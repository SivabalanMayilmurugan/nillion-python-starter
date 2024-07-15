from nada_dsl import *
import hashlib
import random

def nada_main():
    num_participants = 100  # Number of participants
    max_team_size = 5       # Maximum size of a team

    # Define parties (participants)
    parties = [Party(name=f"Participant_{i+1}") for i in range(num_participants)]

    # Generate random participant IDs
    participant_ids = [hashlib.sha256(str(random.randint(1, 10000)).encode()).hexdigest()[:8] for _ in range(num_participants)]

    # Assign participants to teams randomly
    teams = []
    used_ids = set()
    for _ in range(num_participants // max_team_size):
        team = random.sample(participant_ids, max_team_size)
        teams.append(team)
        used_ids.update(team)

    # Handle remaining participants
    remaining_participants = list(set(participant_ids) - used_ids)
    for participant in remaining_participants:
        teams.append([participant])

    # Define secret inputs for team assignments
    outputs = []
    for i, team in enumerate(teams):
        for participant_id in team:
            input_value = participant_id
            secret_input = SecretString(Input(name=f"team_{i}member{participant_id}", party=parties[participant_ids.index(participant_id)], value=input_value))
            outputs.append(Output(secret_input, f"team_{i}member{participant_id}_output", parties[participant_ids.index(participant_id)]))

    return outputs

# Simulated NADA execution environment
def run_nada_program():
    num_participants = 100  # Number of participants
    max_team_size = 5       # Maximum size of a team

    # Generate random participant IDs
    participant_ids = [hashlib.sha256(str(random.randint(1, 10000)).encode()).hexdigest()[:8] for _ in range(num_participants)]

    # Assign participants to teams randomly
    teams = []
    used_ids = set()
    for _ in range(num_participants // max_team_size):
        team = random.sample(participant_ids, max_team_size)
        teams.append(team)
        used_ids.update(team)

    # Handle remaining participants
    remaining_participants = list(set(participant_ids) - used_ids)
    for participant in remaining_participants:
        teams.append([participant])

    return teams

# Running the NADA program to determine team assignments
teams = run_nada_program()

# Display the teams
print("Team Assignments:")
for i, team in enumerate(teams):
    print(f"Team {i + 1}: {team}")