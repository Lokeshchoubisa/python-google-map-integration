import webbrowser
print('enter 1 to see place')
print('enter 2 to view direction')
print('enter 3 to exit')
while True:
    try:
        x=int(input())
    except ValueError:
        x=int(input())
    if x==2:
        print('current location')
        add1=input()
        print('destination')
        add2=input()
        webbrowser.open('https://www.google.com/maps/dir/' + add1+'/'+add2)
        print('thanks')

    if x==1:
        print('enter the location')
        add=input()
        webbrowser.open('https://www.google.com/maps/place/'+add)
        print('thanks for using us')
    if x==3:
        exit()