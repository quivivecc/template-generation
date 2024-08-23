from PIL import Image, ImageDraw, ImageFont
import glob
import json

def draw_text(draw, text, position, font, color="black"):
    draw.text(position, text, fill=color, font=font)

def logo_lookup(team):
    all_files = glob.glob('resources/images/logos/*')
    for i in all_files:
        if team in i:
            return i

def draw_innings(draw, img, innings_data, start_x, start_y, font, line_height, column_gap):

    #Logo lookup
    team_logo_path = logo_lookup(''.join([i for i in innings_data['team'] if not i.isdigit()]).strip())
    team_logo = Image.open(team_logo_path)
    team_logo = team_logo.resize((100, 100))
    img.paste(team_logo, (start_x - 100, start_y - 25), team_logo)

    # Draw team and score
    draw_text(draw, f"{innings_data['team']}", (start_x, start_y), font, color="white")
    draw_text(draw, f"{innings_data['score']}/{innings_data['wickets']} {innings_data['overs']} OV", (start_x  + 580, start_y), font, color="white")
    
    # Draw top scorers and top bowlers in parallel columns
    scorer_y = start_y + 80
    bowler_y = scorer_y
    
    max_items = max(len(innings_data['top_scorers']), len(innings_data['top_bowlers']))
    
    for i in range(max_items):
        if i < len(innings_data['top_scorers']):
            scorer = innings_data['top_scorers'][i]
            draw_text(draw, f"{scorer['name']}      {scorer['stats']}", (start_x - 50, scorer_y), font)
            scorer_y = scorer_y + 65
        
        if i < len(innings_data['top_bowlers']):
            bowler = innings_data['top_bowlers'][i]
            draw_text(draw, f"{bowler['name']}      {bowler['stats']}", (start_x + column_gap + 50, bowler_y), font)
            bowler_y = bowler_y + 65
    
    return scorer_y + (max_items + 1) * line_height

def fill_match_summary_with_image(template_path, output_path, match_data):
    # Open the template image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    
    # Define the font and size
    font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 36)
    
    # Define the initial position and line height
    line_height = 40
    column_gap = 400
    
    # Draw the first innings
    next_y = draw_innings(draw, img, match_data['first_innings'], 160, 180, font, line_height, column_gap)
    
    # Draw the second innings
    next_y = draw_innings(draw, img, match_data['second_innings'], 160, 560, font, line_height, column_gap)
    
    # Draw totals to calculate who won
    first_innings_total = match_data['first_innings']['score']
    second_innings_total = match_data['second_innings']['score']
    result = ""

    if first_innings_total > second_innings_total:
        diff = first_innings_total - second_innings_total
        result = f"{match_data['first_innings']['team']} won by {diff} runs"
    else:
        diff = match_data['first_innings']['wickets'] - match_data['second_innings']['wickets']
        result = f"{match_data['second_innings']['team']} won by {diff} runs"

    # Draw the Man of the Match
    draw_text(draw, result, (300, 960), font)
    draw_text(draw, f"Man of the Match: {match_data['man_of_the_match']}", (300, 1005), font)
    
    # # Open the logo or additional image
    sponsor_logo_path = glob.glob(f'resources/images/logos/{match_data['class']}*')
    sponsor_logo = Image.open(sponsor_logo_path[0])
    
    # # Optional: Resize the logo if needed
    sponsor_logo = sponsor_logo.resize((200, 200))  # Resize to 100x100 pixels (adjust as needed)
    
    # # Paste the logo onto the template image
    img.paste(sponsor_logo, (50, 900), sponsor_logo)  # The third parameter is used for transparency if the image has an alpha channel
    img.paste(sponsor_logo, (800, 900), sponsor_logo)  # The third parameter is used for transparency if the image has an alpha channel
    
    # Save the output image
    img.save(output_path)

# Example match data
with open('matchdata.json') as f:
    match_data = json.load(f)


# Paths to the template, output image, and logo image
template_path = "resources/images/matchsummary_template.png"
output_path = "matchsummary.png"
# logo_path = "team_logo.png"  # Replace with the path to your logo or image

# Fill the match summary and add the logo
fill_match_summary_with_image(template_path, output_path, match_data)
