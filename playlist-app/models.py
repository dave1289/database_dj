"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'

    def __repr__(self):
        p = self
        return f'<PLAYLIST id:{p.id} name:{p.name} description:{p.description}>'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)

    songs = db.relationship('PlaylistSong', backref='playlist')

class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'

    def __repr__(self):
        p = self
        return f'<SONG id:{p.id} title:{p.title} artist:{p.artist}>'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlists_songs'

    def __repr__(self):
        p = self
        return f'<PLAYLIST_SONGS id:{p.id} playlist_id:{p.playlist_id} song_id:{p.song_id}>'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
