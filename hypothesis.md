### Hypothesis

The popularity of a track (`track_popularity`) is influenced by various features in the dataset. Specifically, we hypothesize that:

1. **Track Characteristics**:
   - **Danceability**: Tracks with higher danceability scores are more likely to be popular as they are easier to dance to.
   - **Energy**: Higher energy levels in a track may correlate with higher popularity due to their engaging and lively nature.
   - **Key**: The musical key of a track might have a minor impact on its popularity, with certain keys being more favorable.
   - **Loudness**: Louder tracks might be more popular as they tend to stand out more.
   - **Speechiness**: Tracks with moderate speechiness might be more popular, as they balance between music and spoken word.
   - **Liveness**: Tracks with higher liveness scores might be more popular if they convey a live performance feel.
   - **Valence**: Tracks with higher valence (happiness) scores might be more popular as they evoke positive emotions.
   - **Tempo**: The tempo of a track might influence its popularity, with certain tempos being more appealing.

2. **Track Metadata**:
   - **Track Name**: The name of the track might have a minor impact on its popularity.
   - **Track Artist**: Popularity of the artist might significantly influence the track's popularity.
   - **Track Album Name**: The album name might have a minor impact on the track's popularity.
   - **Track Album Release Date**: The release date might influence popularity, with newer tracks potentially being more popular.
   - **Playlist Genre**: The genre of the playlist might significantly impact the track's popularity, with some genres being more popular than others.
   - **Duration (ms)**: The length of the track might influence its popularity, with certain durations being more favorable.

3. **Categorical Features**:
   - **Tempo Category**: The tempo category might influence the track's popularity.
   - **Loudness Category**: The loudness category might impact the track's popularity.
   - **Release Month**: The month of release might influence the track's popularity, with certain months being more favorable for releases.

By analyzing these features, we aim to build a predictive model that accurately estimates the popularity of a track.