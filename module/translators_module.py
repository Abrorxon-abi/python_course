# # pipenv install tranlators
# # import translators as ts
# # text = 'hello world!'
# # print(ts.translate_text(text, to_language='ru'))
# # proxy
# # re.sub(pattern, replacement, text
# # , count=0, flags=re.)

# import re 
# # string = 'The rain in Spain'
# # t_to_s = 'in'
# # print(re.search(t_to_s, string))
# # print(re.findall(t_to_s, string))
# # print(re.split(t_to_s, string))
# # print(re.split(re.compile(r'in'), string))

# # result = re.sub(
# #     t_to_s, 
# #     '***',
# #     string,
# #     count=2,
# #     flags=re.IGNORECASE
# # )
# # print(result)

# re.compile(r'@([A-Za-z0-9_]+)')
# user_name = '@username'
# print(test(re.search(r'@([A-Za-z0-9_]+)', user_name)))