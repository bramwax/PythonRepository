# #####################################################################################################################
# ====================================================================================== << School Council Elections >>

# ----------------------------------------- << Store list of tutor groups (6 per year groups 7 to 11) >>
tutor_groups = ['7A','7B','7C','7D','7E','7F','8A','8B','8C','8D','8E','8F','9A','9B','9C','9D','9E','9F',
                    '10A','10B','10C','10D','10E','10F','11A','11B','11C','11D','11E','11F']
group_name = ''
group_size = 0
candidate_names,candidate_votes,voter_ids = [],[],[]
# ----------------------------------------------------------------------------------- << Print title >>
print('=' * 80 + '\n' + '<' * 45 + '  School Council Elections 2021  >>' + '\n' + '=' * 80)
# ------------------------------------------------------------------ << Enter & validate tutor group >>
valid_group = False
while not valid_group:
  group_name = input('Enter tutor group: ').upper()
  if group_name not in tutor_groups:
    print('>> Error! Tutor group not recognised...\n')
  else:
    valid_group = True
print('-' * 80)
# ---------------------------------------------------------- << Enter & validate group size (2 to 5) >>
valid_group_size = False
while not valid_group_size:
  group_size = int(input('Enter group size (must be between 2 and 5): '))
  if group_size < 2 or group_size > 5:
    print('>> Error! Outside acceptible range...\n')
  else:
    valid_group_size = True
print('-' * 80)
# >> --------------------------------------------- << Enter & validate number of candidates (1 to 4) >>
valid_number_candidates = False
while not valid_number_candidates:
  number_candidates = int(input('Enter number of candidates (must be between 1 and 4): '))
  if number_candidates < 1 or number_candidates > 4:
    print('>> Error! Outside acceptible range...\n')
  else:
    valid_number_candidates = True
print('-' * 80)
# >> -------------------------------------------------- << Enter candidate names & set votes to zero >>
for i in range(number_candidates):
  candidate_names.append(input(f'Enter name of candidate {i+1}: '))
  candidate_votes.append(0)
# >> ------------------------------------------------------------------------- << Generate voter IDs >>
for i in range(group_size):
  voter_ids.append(group_name + str(i+1))
print('=' * 80)
# >>----------------------------------------- << Check if vote is required (more than one candidate) >>
one_winner = False
if len(candidate_names) == 1:
  one_winner = True
# ===================================================================================================== << Main Loop >>
one_winner = False
while not one_winner:
  # --------------------------------------------------------------------- << Set temporary variables >>
  voter_ids_copy = voter_ids[:] # Copies rather than references
  abstentions = 0
  voted = []
  # ------------------------------------------------- << List candidates and instructions for voting >>
  voting_list = '\nEnter '
  for i in range(len(candidate_names)):
    voting_list += str(i+1) + ' for ' + candidate_names[i] + ', '
  voting_list += 'or 0 to Abstain...'
  print(voting_list)
  print('=' * len(voting_list))
  # -------------------------------------------------------------------------- << Register all votes >>
  while len(voter_ids_copy) > 0:
    # ----------------------------------------------------- << List voter ids still eligible to vote >>
    ids_remaining = '\nVotes left to cast (IDs): ' + ' | '.join(str(value) for value in voter_ids_copy)
    print(ids_remaining + '\n' + '-' * (len(ids_remaining)))
    # ----------------------------------------------------------------- << Enter & validate voter ID >>
    valid_id = False
    while not valid_id:
      tmp_id = input('Enter voter ID: ').upper()
      if tmp_id in voted:
        print('Error! Duplicate vote...\n')
      elif tmp_id not in voter_ids:
        print('Error! ID not recognised...\n')
      else:
        valid_id = True
    # --------------------------------------------------------------------------- << Record voter id >>      
    voted.append(tmp_id)
    voter_ids_copy.remove(tmp_id)
    # --------------------------------------------------------------------- << Enter & validate vote >>      
    valid_vote = False
    while not valid_vote:
      vote_cast = int(input('Enter vote: '))
      if vote_cast < 0 or vote_cast > len(candidate_names):
        print('Error! Invalid candidate\n')
      else:
        valid_vote = True
    # ---------------------------------------------------------------- << ecord vote/abstention cast >>      
    if vote_cast == 0:
      abstentions += 1
    else:
      candidate_votes[vote_cast-1] = candidate_votes[vote_cast-1] + 1
  # ----------------------------------------------------------------- << Calculate the winning score >>      
  winning_score = 0
  for i in candidate_votes:
    if i > winning_score:
      winning_score = i
  # ----------------------------------------------------------- << Locate and store names of winners >>
  winner_names = []
  winner_votes = []
  for i in range(len(candidate_votes)):
    if candidate_votes[i] == winning_score:
      winner_names.append(candidate_names[i])
      winner_votes.append(candidate_votes[i])
  # --------------------------------------------------------------- << Calculate & store total votes >>
  total_votes = 0
  for i in candidate_votes:
    total_votes += i
  print('=' * len(voting_list))
  # ------------------------------------------------- << Print group name, total votes & abstentions >>
  print(f'\nTutor group: {group_name} | Votes cast: {total_votes} | Abstentions: {abstentions}')
  print('-' * len(voting_list))
  # ------------------------------------------------------------- << Print total votes & abstentions >>
  for i in range(len(candidate_names)):
    tmp_percent = round(candidate_votes[i] / total_votes * 100,2)
    output = f'{candidate_names[i]} recieved {tmp_percent}% of the votes with {candidate_votes[i]} vote'
    if candidate_votes[i] > 1:
      output += 's'
    print(output)
  # ------------------------------------------------------------ << Determine if recount is required >>
  if len(winner_names) > 1:
    print('\n' + '=' * 80 + '\nThere is no clear winner')
    print('We will now do a recount for the winning candidates!\n' + '=' * 80)
  # ------------------------------------------------------------- << Reset candidate_names and votes >>
    candidate_names = winner_names[:]
    candidate_votes = []
    for i in winner_names:
      candidate_votes.append(0)
  else:
    one_winner = True

# ========================================================================================= << Print election result >>
print('=' * len(voting_list))
print(f"Congratulations, {group_name}'s school council rep is {winner_names[0]}")
print('=' * len(voting_list))
# #####################################################################################################################
