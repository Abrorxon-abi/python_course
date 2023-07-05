nums_written_by_word = ['One', 'Two', 'Three',
                        'Four', 'Five', 'Six',
                        'Seven',	 'Eight', 'Nine',
                        'Ten', 'Eleven', 'Twelve',
                        'Thirteen', 'Fourteen', 'Fifteen',
                        'Sixteen', 'Seventeen', 'Eighteen',
                        'Nineteen', 'Twenty']

num_of_letters = list(map(len, nums_written_by_word))
gg = sum(map(int, num_of_letters))
print(gg)
