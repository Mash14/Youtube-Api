# Youtube Search

The name of the project is Youtube Search

## Description

The project is used to showcase the use of youtube api to show search for videos and embed and show them in a django project.   

## Technologies Used

- Django
- Python3
- Youtube Api

## Installation

- First go to Google Developers page login and create a new project.
    ```
    [Google developer](https://console.developers.google.com/)
    ```
- Then go to Enable Api and Services and find YouTube Data API-v3, enable it, then create credentials then you will get the youtube api key.
- Git clone the project in you repository
    ```
    git clone https://github.com/Mash14/Youtube-Api.git
    ```
- Create an .env file in the root of the project 
    ```
    YOUTUBE_API_KEY='<your-youtube-api-key>'
    ```
- Create a virtual environment and run it
    ```
    virtualenv virtual
    
    source virtual/bin/activate
    ```
- Install dependencies in the requirements.txt file
    ```
    pip install -r requirements.txt
    ```
- Run the application
    ```
    python3 manage.py runserver
    ```

## Screenshots

The Home Page
![Home Page](/static/img/b4_search.png)

Home Page After Search
![Home Page After Search](/static/img/after_search.png)

Single Searched Video
![Single Seached Video](/static/img/single_video.png)

## Developer's Details

The author of this project was Alan Macharia

## Contact information

You can reach the developer by
- Email: mashalonzo741@gmail.com
- Tel: 0704485919 

## Known Bugs

There are no known bugs 

## License and Copyright information

The license information can be found here: [MIT-Lisence](https://opensource.org/licenses/MIT)

Copyright (c)_18/12/2022__Alan Macharia_