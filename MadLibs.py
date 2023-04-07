
#import modules
from tkinter import *

#create display windows
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
Label(root, text = 'Mad Libs Generator \n Have Fun!', font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One:', font = 'arial 15 bold'). place (x=40, y=80)

#define madlib function 1
def madlib1():

    adjective = input('Enter an adjective: ')
    food_1 = input('Enter a Food (plural): ')
    verb = input('Enter a Verb: ')
    Saying = input('Enter a Saying: ')
    Noun = input('Enter a Noun: ')
    food_2 = input('Enter a Food (plural): ')
    color = input('Enter a color: ')
    sywri = input('Enter Something you would ride in: ')
    animal = input('Enter an Animal: ')
    person = input('Enter a Person: ')
    print ( 'Today I went to my favorite Taco Stand called the '+adjective+ ' ' + animal +'. Unlike most food stands, they cook and prepare' 
           'the food in a ' + sywri + ' while you ' +verb+'. The best thing on the menu is the '+ color+' '+Noun+'. ' 
           'Instead of ground beef they fill the taco with '+ food_2 + ', cheese, and top it off with a salsa made from '+food_1+'. '
           'If that does not make your mouth water, then it is just like '+person+' always says: '+Saying+'!'
    )

#define madlib function 2
def madlib2():

    occupation = input('Enter a Occupation (a job): ')
    noun_1 = input('Enter a Noun: ')
    adjective_1 = input('Enter an Adjective: ')
    noun_2 = input('Enter a Noun: ')
    verb_1 = input('Enter a Verb: ')
    adjective_2 = input('Enter an Adjective: ')
    noun_3 = input('Enter a Noun: ')
    verb_2 = input('Enter a Verb: ')
    noun_4 = input('Enter a Noun: ')
    verb_3 = input('Enter a Verb: ')
    print ('Today a '+occupation+' named '+noun_4+' came to our school to talk to us about her job. '
           'She said the most important skill you need to know to do her job is to be able to '+verb_2+
           ' around (a) '+adjective_1+' '+noun_3+'. She said it was easy for her to learn her job because '
           'she loved to '+verb_1+' when she was my age--and that helps a lot! If you are considering her profession, '
           'I hope you can be near (a) '+adjective_2+' '+noun_1+'. That is very important! If you get too distracted in '
           'that situation you will not be able to '+verb_3+' next to (a) '+noun_2+'!'
    )

#define madlib function 3
def madlib3():

    animals = input('Enter animals: ')
    feeling = input('Enter a Feeling: ')
    things_1 = input('Enter Things(plural): ')
    professional = input('Enter a Professional(like "Baker"): ')
    piece_clothing = input('Enter a Piece of Clothing: ')
    things_2 = input('Enter Things(plural): ')
    person = input('Enter a Person: ')
    place = input('Enter a Place: ')
    verb = input('Enter a Verb (ending in "ing"): ')
    food = input('Enter a Food: ')
    print ("Say '"+food+",' the photographer said as the camera flashed! "+person+" and I had gone to "+place+" to get our photos taken today. "
           "The first photo we really wanted was a picture of us dressed as "+animals+" pretending to be a "+professional+". When we saw the proofs "
           "of it, I was a bit "+feeling+" because it looked different than in my head. (I hadn't imagined so many "+things_1+" behind us.) "
           "However, the second photo was exactly what I wanted. We both looked like "+things_2+" wearing "+piece_clothing+" and "+verb+"--exactly what I "
           "had in mind!" 
        
    )

#define buttons
Button(root, text= 'Tacos', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=110, y=120)
Button(root, text= 'Jobs', font ='arial 15', command= madlib2, bg = 'ghost white').place(x=115, y=180)
Button(root, text= 'Photo Shoot', font ='arial 15', command= madlib3, bg = 'ghost white').place(x=80, y=240)

#run main function
root.mainloop()
