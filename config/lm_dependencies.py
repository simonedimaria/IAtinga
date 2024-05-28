import languagemodels as lm

lm.config['instruct_model'] = 'LaMini-Flan-T5-248M'

lm.store_doc("triggering model and other stuff download")

context = lm.get_doc_context("model")

lm.extract_answer("model", context)

lm.code("""
a = 2
b = 5
# Swap a and b
""")

# download the models and other necessary files on the first run
