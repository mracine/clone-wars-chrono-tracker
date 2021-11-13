# Star Wars: The Clone Wars Chronological Tracker
For those who want to watch Star Wars: The Clone Wars in chronological order and want to track overall progress through the series, as well as the next episode chronologically based on your current progress.

For clarification, this application does not integrate with whatever viewing platform you are watching the series on, it is simply a way of manually tracking your progress.

*Please keep in mind development for this application is mostly still in progress. Running this application should be mostly fine but the code is not thoroughly tested and there may be some issues. Additionally, the frontend design needs some improvement and there are features that have not been implemented yet.*

## Installation
Currently the only targeted build is for Alpine Linux on Docker (I plan on making builds for different platforms). Also, there is currently no image published to Dockerhub (subject to change) so you will have to build the container locally.

```
git clone https://github.com/mrracine/clone-wars-chrono-tracker
cd clone-wars-chrono-tracker
docker-compose up -d
```

## Development
This application is built on Flask for the API service and Vue.js for the frontend.

<!-- this section under construction -->

## TODO
Development thoughts and potential features (until I create the issues in Github).

### Backend features/requests
- An instance folder location should be decided inside the container and mapped in the docker-compose.yml
- The database needs to be initialized and created if it doesn't exist
- Put clonewars.csv in better location.
- Should docker copy over the instance folder?
- Is there a solution that doesn't involve Flask-Cors?
- Is uwsgi a better server implementation than gunicorn?
- Is there a way to add in only site config for nginx (leave default.conf)
- Are there any endpoints that would be useful?
- Is the "tracker" blueprint really necessary?
- Add different users that have different tracking progress
- Integrations for TVDB? Plex? Jellyfin?
- Should figure out a way to package/run locally
- Potentially abstract it to allow different viewing orders of shows?

### Frontend features/requests
- Progress bar in frontend?
- Reset progress + confirmation prompt
- Recently viewed tab?
- Investigate using axios for async requests instead
- General UI improvement
- Add some rendering/conditions for mobile devices

*Good soldiers follow orders.*
