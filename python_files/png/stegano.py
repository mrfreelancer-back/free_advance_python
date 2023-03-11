from stegano import lsb

secure_text = lsb.hide('file.png', 'Ali')
secure_text.save('stegano.png')

obvious_msg = lsb.reveal('stegano.png')
print(obvious_msg)