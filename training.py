###learnign arguments and keyword arguments###

#python allows for use of variable length list as arguments

def main():
    kitten('mewo', 'poopy', 'splonky')

def kitten(args):
    #this is just checking to see if the length of the list is greater than 0
    if len(args):
        for i in args:
            print(args)
        else:
            print('Meow')

if __name__ == '__main__':
    main()


##because the keywords are in the form of a dictionary usee ** if it was a list use *
def main():
    x == dict(Buffy='meow', Zilla='grr', Splonk='Splonky')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('{} says {}'.format(k, kwargs[k])
   else:
        print('poopu')
        
if __name__ == '__main__':
    main()
