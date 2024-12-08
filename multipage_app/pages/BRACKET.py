import streamlit as st

st.title("BRACKET")

# Initialize session state for participants if it doesn't exist
if 'participants' not in st.session_state:
    st.session_state.participants = []

with st.form("my_form"):
    num_participants = st.number_input("Enter the number of participants (even number):", min_value=2, step=2)
    submitted = st.form_submit_button("Submit")

if submitted:
    if num_participants % 2 == 0:
        # Ensure the session state has the correct number of participants
        if len(st.session_state.participants) != num_participants:
            st.session_state.participants = [''] * num_participants

        # Create text inputs for participant names
        for i in range(num_participants):
            st.session_state.participants[i] = st.text_input(f"Participant {i+1}:", value=st.session_state.participants[i])

        # Check if all participant names are filled
        if all(name for name in st.session_state.participants):
            # Create the bracket structure
            bracket = {}
            round_num = 1
            participants = st.session_state.participants.copy()  # Use a copy of the participants list
            while len(participants) > 1:
                bracket[round_num] = []
                for i in range(0, len(participants), 2):
                    matchup = [participants[i], participants[i + 1]]
                    bracket[round_num].append(matchup)
                participants = [matchup[0] for matchup in bracket[round_num]]
                round_num += 1

            # Display the bracket
            st.write("Bracket:")
            for round in bracket:
                st.write(f"Round {round}:")
                for matchup in bracket[round]:
                    st.write(f"- {matchup[0]} vs {matchup[1]}")
        else:
            st.warning("Please fill in all participant names.")
    else:
        st.error("Please enter an even number of participants.")