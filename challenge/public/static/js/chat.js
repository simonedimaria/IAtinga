const chatExamples = {

    "default": [
        "what is the airspeed velocity of an unladen swallow?",
        "summarize this for me",
        "who are you?"
    ],
    "iotinga": [
        "Who is the Iotinga's CBO?",
        "What's Alerighi's role at Iotinga?",
        "Alerighi's Guide on how to Bypassing RAI License fees",

    ],
    "iotinga-eng": [
        "Who is the Iotinga's CBO?",
        "What's Alerighi's role at Iotinga?",
        "Alerighi's Guide on how to Bypassing RAI License fees",
        "How does Iotinga simplify business processes?",
        "What are the benefits of working with Iotinga?",
        "What does Iotinga specialize in?",
        "What's Iotinga's philosophy?",
        "How does Iotinga bring innovation to market?",
        "Which industries does Iotinga cover?"

    ]

}
function getRandomElements(arr, numElements) {
    // Randomize the array
    const randomizedArray = arr.sort(() => Math.random() - 0.5);
    
    // Return the first numElements elements from the randomized array
    return randomizedArray.slice(0, numElements);
}


$(document).ready(function () {
    let params = new URLSearchParams(window.location.search);

    if (params.has('topic')) {
        const topic = params.get('topic');
        let examples = chatExamples[topic] || chatExamples['default'];
        examples=getRandomElements(examples, 3);
        $('#topic').text(topic);

        $('.chat-example').each(function (index) {
            $(this).text(examples[index]);
        });
    } else {
        const examples = chatExamples['default'];

        $('#topic').text('Unknown');

        $('.chat-example').each(function (index) {
            $(this).text(examples[index]);
        });
    }

    $('.chat-example').on('click', function () {
        $('#prompt').val($(this).text());
    });

    $('#prompt').on('input keydown', function (e) {
        $('#resp-msg').hide();

        if (e.key === 'Enter' && e.ctrlKey) {
            $(this).val(function (i, val) {
                return val + "\n";
            });
        }
        else if (e.key === 'Enter' && !e.ctrlKey) {
            let prompt = $('#prompt').val().replace(/\n/g, '');
            if (prompt !== '') submitPrompt();
        }

        let count = ($('#prompt').val().match(/\n/g) || []).length;
        if (count > 1) {
            $(this).height('auto').height(this.scrollHeight);
        }
    });

    $('#prompt-btn').on('click', submitPrompt);

    window.observer = new MutationObserver(scrollToBottom);
    window.lastScrollHeight = -1;
});

const toggleProps = (state) => {
    $('#prompt').prop('disabled', state);
    $('#prompt-btn').prop('disabled', state);
    if (state) {
        $('#loading').show();
    }
    else {
        $('#loading').hide();
    }
}

const submitPrompt = async () => {
    toggleProps(true);

    if (!$('#chat-placeholder').hasClass('hidden')) {
        $('#chat-placeholder').addClass('hidden');
    }

    card = $('#resp-msg');
    card.hide();

    let prompt = $('#prompt').val().replace(/\n/g, '');

    if (prompt === '') {
        card.text('Please enter a prompt.');
        card.attr('class', 'alert alert-danger');
        card.show();
        toggleProps(false);
        return;
    }
    else if (prompt.length > 512) {
        card.text('The prompt is too long. Please enter a prompt that is less than 1024 characters.');
        card.attr('class', 'alert alert-danger');
        card.show();
        toggleProps(false);
        return;
    }

    let randomQid = Math.floor(Math.random() * 1000000000);
    let randomAid = Math.floor(Math.random() * 1000000000);

    let userBubble = `
    <div class="bubble user-bubble">
        <div class="d-flex align-items-center">
            <span class="avatar">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0ec80e" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </span>
            <span class="bo fw-bold ms-3 fs-6">You</span>
        </div>
        <p class="message user-message" id="${randomQid}">
            
        </p>
    </div>`;

    $('#chat-bubbles').prepend(userBubble);
    $(`#${randomQid}`).text(prompt);

    let gptBubble = `
    <div class="bubble gpt-bubble">
        <div class="d-flex align-items-center">
        <span class="avatar gpt-avatar" style="background-color: white; padding: 2px; border-radius: 50%;">            <img src="/static/images/logo.png" alt="Logo" width="24" height="24">
        </span>
            <span class="bo fw-bold ms-3 fs-6">IAtinga</span>
        </div>
        <p class="message gpt-message" id="${randomAid}">

        </p>
    </div>`;

    $('#chat-bubbles').prepend(gptBubble);

    window.observer.disconnect();
    window.observer.observe($(`#${randomAid}`)[0], { childList: true, subtree: true });

    await fetch('/api/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
    }).then(async (res) => {
        if (res.status === 200) {
            let data = await res.json();
            card.hide();
            let typed = new Typed($(`#${randomAid}`)[0], {
                strings: [data.answer],
                typeSpeed: 15,
                showCursor: false,
                onStringTyped: function () {
                    window.observer.disconnect();
                    toggleProps(false);
                }
            });
        } else {
            let data = await res.json();
            card.text(data.message ? data.message : 'An error occurred, if this error persists, try a different prompt.');
            card.attr('class', 'alert alert-danger');
            card.show();
            toggleProps(false);
        }

    }).catch((err) => {
        console.log(err);
        card.text('An error occurred, if this error persists, try a different prompt.');
        card.attr('class', 'alert alert-danger');
        card.show();
        toggleProps(false);
    });
}


const scrollToBottom = () => {
    if (window.lastScrollHeight < $('#chat-bubbles')[0].scrollHeight) {
        $('.chat-row').animate({ scrollTop: parseInt($('#chat-bubbles')[0].scrollHeight) }, 1000);
        window.lastScrollHeight = $('#chat-bubbles')[0].scrollHeight;
    }
}
