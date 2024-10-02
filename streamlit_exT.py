import streamlit as st 
import pandas as pd  
import json 
import matplotlib.pyplot as plt 
import matplotlib.patches as patches 
import numpy as np 


# Define your exT visualization function
def exT_vis(df, player_name, season='AFL Season 2024'):
    # Create a subplot with 2 rows and 1 column
    fig = plt.figure(figsize=(8, 12))
    fig.patch.set_facecolor('#0C0D0E')

   # Top row for the team names and score
    ax1 = fig.add_axes([0, 0.7, 1, .2])
    ax1.set_facecolor('#0C0D0E')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    # Player name and season
    ax1.text(x=0.5, y=.85, s=f'{player_name}', fontsize=20, fontweight='bold', color='white', ha='center')
    ax1.text(x=0.5, y=.7, s=f'All Disposals in {season}', fontsize=14, fontweight='bold', color='white', ha='center')
    ax1.text(x=0.25, y=0.5, s=f'Low ExT', fontsize=12, color='white', ha='center')

    # Adding scatter points between the texts
    for i, size in enumerate([100, 200, 300, 400, 500]):
        ax1.scatter(x=0.37 + i*0.05, y=0.53, s=size, color='#0C0D0E', edgecolor='white', linewidth=.8)

    ax1.text(x=0.75, y=0.5, s=f'High ExT', fontsize=12, color='white', ha='center')

    ax1.text(x=0.45, y=0.27, s=f'exT Loss', fontsize=10, color='white', ha='right')
    ax1.scatter(x=0.47, y=0.3, s=100, color='red', edgecolor='white', linewidth=.8, alpha=.7)
    ax1.scatter(x=0.53, y=0.3, s=100, color='lightblue', edgecolor='white', linewidth=.8)
    ax1.text(x=0.55, y=0.27, s=f'exT Gain', fontsize=10, color='white', ha='left')

    ax1.set_axis_off()

    # Drawing the pitch visualization
    ax2 = fig.add_axes([0, 0, 1, 0.7])

    length = 140
    width = 165
    oval = patches.Ellipse((0, 0), width, length, edgecolor='white', facecolor='none', linewidth=1)
    ax2.add_patch(oval)

    # Customize appearance
    ax2.set_facecolor('#0C0D0E')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_xlim([-width / 2 - 10, width / 2 + 10])
    ax2.set_ylim([-length / 2 - 10, length / 2 + 10])
    ax2.set_aspect('equal', 'box')

        # Drawing the centre square
    centre_square = patches.Rectangle((-25, -25), 50, 50, edgecolor='white', facecolor='none', linewidth=1)
    ax2.add_patch(centre_square)

    
    
    # Drawing right goals
    ax2.plot([82, 67],    # x coordinates
            [-5, -5],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
    
    ax2.plot([82, 67],    # x coordinates
            [5, 5],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
    
    ax2.plot([81, 72],    # x coordinates
            [10, 10],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
    
    ax2.plot([81, 72],    # x coordinates
            [-10, -10],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
    
    # Drawing left goals
    ax2.plot([-82, -67],    # x coordinates
            [-5, -5],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
    
    ax2.plot([-82, -67],    # x coordinates
            [5, 5],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
    
    ax2.plot([-81, -72],    # x coordinates
            [10, 10],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
    
    ax2.plot([-81, -72],    # x coordinates
            [-10, -10],     # y coordinates
            color='white', # Line color
            linewidth=2)   # Line width
   

    # Define the right arc parameters
    center_x = 70   # X coordinate of the center of the arc
    center_y = 0   # Y coordinate of the center of the arc
    radius = 37  # Radius of the arc
    theta_start = np.pi / 2    # Starting angle (45 degrees, in radians)
    theta_end = 3 * np.pi / 2  # Ending angle (135 degrees, in radians)

    # Create theta values for the arc
    theta = np.linspace(theta_start, theta_end, 100)

    # Parametric equations for the arc
    x_arc = center_x + radius * np.cos(theta)
    y_arc = center_y + radius * np.sin(theta)

    # Plot the arc
    ax2.plot(x_arc, y_arc, color='white', linewidth=2)
    
   
        # Define the left arc parameters
    left_center_x = -70   # X coordinate of the center of the arc (on the left side)
    left_center_y = 0     # Y coordinate of the center of the arc
    left_radius = 37      # Radius of the arc
    left_theta_start = np.pi / 2    # Starting angle (90 degrees, in radians)
    left_theta_end = 3 * np.pi / 2  # Ending angle (270 degrees, in radians)

    # Create theta values for the arc
    left_theta = np.linspace(left_theta_start, left_theta_end, 100)

    # Parametric equations for the arc (flipped horizontally)
    x_arc_flipped = left_center_x - left_radius * np.cos(left_theta)  # Negate cos(theta) to flip the arc horizontally
    y_arc_flipped = left_center_y + left_radius * np.sin(left_theta)

    # Plot the flipped arc
    ax2.plot(x_arc_flipped, y_arc_flipped, color='white', linewidth=2)
    
    ax2.arrow(-30,               #x start point
              75,              #y start point (around the top of the field)
              60,              #change in x (20 units to the right)
              0,               #change in y (no vertical movement)
              head_width=2.5,    #arrow head width
              head_length=2.5,   #arrow head length
              width=0.5,         #arrow shaft width
              color='white')   #color of the arrow
                 #arrow stem width
    

    # Filter data for the player
    filtered_df_gain = df[(df['player_name'] == player_name) & (df['exT_gain'] > 0)]
    filtered_df_loss = df[(df['player_name'] == player_name) & (df['exT_gain'] < 0)]

    # Plot the data points
    ax2.scatter(filtered_df_gain['x'], filtered_df_gain['y'], s=300 * filtered_df_gain['exT_gain'], color='lightblue',
                edgecolor='white', linewidth=1.5, alpha=0.8)
    ax2.scatter(filtered_df_loss['x'], filtered_df_loss['y'], color='red', s=-300 * filtered_df_loss['exT_gain'],
                edgecolor='white', linewidth=1.5, alpha=0.8)

    # Add additional text and details here as needed...
    ax2.set_axis_off()

        # Calculate stats for the player
    # Add another axis for the stats
    ax3 = fig.add_axes([0, 0.65, 1, .1])
    ax3.set_facecolor('#0C0D0E')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    #points_added = (df[df['playerName.surname'] == surname]['exT_gain'].groupby('roundNumber').mean() * 6).mean()
    points_added = round(df[df['player_name'] == player_name].groupby(['roundNumber', 'player_name'])['exT_gain'].sum().mean()*6, 2)
    exT_rank = round(df[df['player_name'] == player_name]['rank'].mean())

    total_players = df['player_name'].nunique()

    ax3.text(x=0.36, y=.5, s='exT Pts Per/G', fontsize=20, fontweight='bold', color='white', ha='left')
    ax3.text(x=0.39, y=0, 
             s=r'$\mathbf{' + f'{points_added:.2f}' + r' \; \left(' + f'{exT_rank:.0f}' + r' / ' + f'{total_players:.0f}' + r'\right)' + '}$',
             fontsize=16, color='red', ha='left')

    ax3.text(x=0.49, y=-0.1, 
             s='rank',
             fontsize=8, color='red', ha='left')

    ax3.set_axis_off()



    # Use Streamlit to display the figure
    st.pyplot(fig)

# Streamlit interface
st.title("AFL Season 2024 - exT")
st.subheader("Filter to a player to review their exT Threat across the 2024 season")

df = pd.read_csv('/Users/jamesives/ExpectedThreat.csv')
df['player_name'] = df['playerName.givenName'] + " " + df['playerName.surname']

# First, calculate the total exT_gain for each player (by full name)
df['total_exT_gain'] = df.groupby(['playerName.surname', 'playerName.givenName'])['exT_gain'].transform('sum')

# Then, rank players based on their total exT_gain
df['rank'] = df['total_exT_gain'].rank(method='dense', ascending=False)

player_name = st.selectbox('Select a player', df['player_name'].sort_values().unique())

# Call the visualization function with the selected player
exT_vis(df, player_name)
