# Let's do thiss
i=0

def correct(a,b):
    global i 
    if a==b:
        i+=1

        return"Thats correct!"

    else:
        return "Oops sorry you were wrong"
# first one: predict the output
# (i)
a = [1, 2, 3]
a1=a*2
print(a1)
b=[1,2,3,1,2,3]
print(correct(a1,b))
print(f"TOTAL SCORE: {i}\n")

# (ii)
def mystery(x):
    return x * 2

w=mystery("2")
v="22"
print(correct(w,v))

print(f"TOTAL SCORE {i}\n")

# (iii)
try:
  for i in range(3):
    print(i, end="-")
  else:
    print("Done")
except:
   print("This is invalid code")

print("ans: THE ABOVE CODE'S OUTPUT IS: 0-1-2-Done")
i+=1
print(f"TOTAL SCORE {i}\n")

# second one: write the code of the given
'''(i)Even-Odd counter: Take a list of numbers from the user and
print how many are even and how many are odd'''

user=int(input("How many numbers do you need?: "))
even=0
odd=0
for i in range(1,user+1):
    try:
        g=int(input("Enter a number: "))
        if g%2==0:
            even+=1
        elif g%2!=0:
            odd+=1

    except ValueError as e:
      print(f"Error: Invalid input. Details: {e}")

print(f"There are {even} even numbers and {odd} odd numbers")

'''(iii)Input a sentence and reverse the order of words.'''
li=input("Enter the sentence to be reversed(by word): ")
liv=li.split()
liv.reverse()    
print(" ".join(liv))

'''Write a function that counts how many times each character appears in a string.'''
try:
    s=input("Enter a sentence: ")
    p=s.replace(" ","")
    v={}
    for i in p:
        c=p.count(i)

        if i not in v:
            v[i]=c
        
    print(v)
except Exception as e:
    print("Invalid input: {e}")


'''some practice of Dictionaries'''
d={"a":1,"b":2,"c":3}
print(d.keys())
print(d.values())
for i in d:
    print(f'{i}.{d[i]}')
r=["Apples","Pineapples","Grapefruits","Pears","Oranges","Carrot"]

for i,j in enumerate(r,start=1):
    print(f"{i}. {j}") 









        
        


