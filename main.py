import sample

msg = sample.core.get_hmm()

if sample.helpers.get_answer():
    print(msg)
else:
    print('no hmm here...')