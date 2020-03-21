import re

class WordsToNumbers():
    """A class that can translate strings of common English words that
    describe a number into the number described
    """
    
    __ones__ = { 'one':   1, 'eleven':     11,
                 'two':   2, 'twelve':     12,
                 'three': 3, 'thirteen':   13,
                 'four':  4, 'fourteen':   14,
                 'five':  5, 'fifteen':    15,
                 'six':   6, 'sixteen':    16,
                 'seven': 7, 'seventeen':  17,
                 'eight': 8, 'eighteen':   18,
                 'nine':  9, 'nineteen':   19 }
    
    # a mapping of digits to their names when they appear in the 'tens'
    # place within a number group
    __tens__ = { 'ten':     10,
                 'twenty':  20,
                 'thirty':  30,
                 'forty':   40,
                 'fifty':   50,
                 'sixty':   60,
                 'seventy': 70,
                 'eighty':  80,
                 'ninety':  90 }
    
    # an ordered list of the names assigned to number groups
    __groups__ = { 'thousand':  1000,
                   'million':   1000000,
                   'billion':   1000000000,
                   'trillion':  1000000000000 }

    
    __groups_re__ = re.compile(
        r'\s?([\w\s]+?)(?:\s((?:%s))|$)' %
        ('|'.join(__groups__))
        )

    
    #      group's tens- and ones-place value
    __hundreds_re__ = re.compile(r'([\w\s]+)\shundred(?:\s(.*)|$)')

    
    #    1-the tens
    #    2-the ones
    __tens_and_ones_re__ =  re.compile(
        r'((?:%s))(?:\s(.*)|$)' %
        ('|'.join(__tens__.keys()))
        )

    def parse(self, words):
        
        words = words.lower()
        
        groups = {}        
        
        num = 0
        
        for group in WordsToNumbers.__groups_re__.findall(words):
            
            group_multiplier = 1
            if group[1] in WordsToNumbers.__groups__:
                group_multiplier = WordsToNumbers.__groups__[group[1]]
            
            group_num = 0
            # get the hundreds for this group
            hundreds_match = WordsToNumbers.__hundreds_re__.match(group[0])
            
            tens_and_ones = None
            # if there is a string in this group matching the 'n hundred'
            
            if hundreds_match is not None and hundreds_match.group(1) is not None:
                
                group_num = group_num + \
                            (WordsToNumbers.__ones__[hundreds_match.group(1)] * 100)
                
                tens_and_ones = hundreds_match.group(2)
            else:
            
                tens_and_ones = group[0]
            # if the 'tens and ones' string is empty, it is time to
            # move along to the next group
            if tens_and_ones is None:
                # increment the total number by the current group number, times
                # its multiplier
                num = num + (group_num * group_multiplier)
                continue
            # look for the tens and ones ('tn1' to shorten the code a bit)
            tn1_match = WordsToNumbers.__tens_and_ones_re__.match(tens_and_ones)
            # if the pattern is matched, there is a 'tens' place value
            if tn1_match is not None:
                # add the tens
                group_num = group_num + WordsToNumbers.__tens__[tn1_match.group(1)]
                # add the ones
                if tn1_match.group(2) is not None:
                    group_num = group_num + WordsToNumbers.__ones__[tn1_match.group(2)]
            else:
            # assume that the 'tens and ones' actually contained only the ones-
            # place values
                group_num = group_num + WordsToNumbers.__ones__[tens_and_ones]
            # increment the total number by the current group number, times
            # its multiplier
            num = num + (group_num * group_multiplier)
        #the result
        return num



###main function###
# Python Program - Pattern Program 
        
k = 0
rows = 10
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
print("program by UTKRISHT SHARMA \n utkrishtsharma93@gmail.com \n http://utkrisht.ml \n \n \n \n \n ")    


#main func
if __name__ == "__main__":
    # here is an example you can use to test the results
    num = input("enter  number in word form :")
    wtn = WordsToNumbers()
    print (num, ": ", wtn.parse(num))