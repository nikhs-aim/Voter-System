import sys
organizer='Anonymous'
instructions='''INSTRUCTIONS: \n1. A voter can vote for only one candidate.
2. A voter can only vote once.'''
a='''\nThe candidates are A and B.\nPress a to vote for A.\nPress b to vote for B'''
alluserlist=[]
votes_for_a=0
votes_for_b=0
while True:
  want=input('\nPress v to vote (If pressed any, you will be directed to Result section. Note that, only organizers are allowed to see the results): ')
  if want=='v':

   user = input('\nenter your name to vote: ')
   if user not in alluserlist:
        print(f'\nWelcome {user} to the voting poll! you can now vote for your candidate.\n')
        print(instructions)
        print(a)
        alluserlist.append(user)
        while True:
            voter=input('\nEnter your choice: ' )
            if voter=='a':
              votes_for_a+= 1
              print('you have voted for A. Please wait for the results.')
              break
            elif voter=='b':
              votes_for_b+= 1
              print('you have voted for B. Please wait for the results.')
              break
            else:
              print('invalid input')
              continue
   else:
       print('you have already voted!')
  else:
     print('\nORGANIZERS SECTION: ')
     confirm=input('Enter your name: ')
     if confirm==organizer:
         print('\nRESULTS:')
         if votes_for_a > votes_for_b:
             print(f'A has won with {votes_for_a} votes!\nCONGRATULATIONS A')
             sys.exit()
         elif votes_for_b > votes_for_a:
             print(f'B has won with {votes_for_b} votes!\nCONGRATULATIONS B')
             sys.exit()
         elif votes_for_b==0 and votes_for_a==0:
             print('No one has voted yet!')
         else:
             print('The results are tied!')
             sys.exit()
     else:
         print('Sorry ! You are not the organizer.')
         continue




