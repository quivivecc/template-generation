# template-generation

The script helps to create match summary based on JSON input.

### Sample JSON
```
{
    'class': 'Eersteklass',
    'first_innings': {
        'team': 'Team A',
        'score': 250,
        'wickets': 8,
        'overs': 49.5,
        'top_scorers': [{
            'name': 'Player X',
            'stats': '95 (60)'
        },{
            'name': 'Player Y',
            'stats': '50 (75)'
        },{
            'name': 'Player Z',
            'stats': '25 (40)'
        }],
        'top_bowlers': [{
            'name': 'Player A',
            'stats': '8-2-45-3'
        },{
            'name': 'Player B',
            'stats': '7-0-35-1'
        },{
            'name': 'Player C',
            'stats': '10-0-43-1'
        }]
    },
    'second_innings': {
        'team': 'Team B',
        'score': 245,
        'wickets': 10,
        'overs': 49.3,
        'top_scorers': [{
            'name': 'Player D',
            'stats': '70 (60)'
        },{
            'name': 'Player E',
            'stats': '45 (75)'
        },{
            'name': 'Player F',
            'stats': '33 (40)'
        }],
        'top_bowlers': [{
            'name': 'Player G',
            'stats': '8-2-25-3'
        },{
            'name': 'Player H',
            'stats': '10-1-40-2'
        },{
            'name': 'Player I',
            'stats': '7-0-28-1'
        }]
    },
    'man_of_the_match': 'Player X'
}
```

### Notes

* Match summary template is stored under resources/images/matchsummary_template.png
* Logos of the teams and sponsors are stored under resources/images/logos/
* As of now, the JSON needs to be manually filled in. WIP: API integration with resultsvault to fet the match details and fill in deatils automatically.
* Value of the field class in the JSON decides which sponsor logo to be used
* `font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 36)` value of this changes according to the type of OS
    ```
        Windows: C:\Windows\Fonts\arial.ttf
        MacOS: /Library/Fonts/Arial Unicode.ttf
        Linux: /usr/share/fonts/arial.ttf
    ```
* Script needs to be updated, when we use new match summary template as the axes co-ordinates are based on the matchsummary_template.png file under resources/images