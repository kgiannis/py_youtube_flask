from pytube import YouTube
from pytube import exceptions
from flask import Flask
from flask import jsonify

URL_PREFIX = 'https://www.youtube.com/watch?v='
response = {}

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/<movie_id>')
def get_movie_info(movie_id=None):
    """
    Get information of a video based on movie ID
    :param movie_id: the ID of the video
    :return: JSON representation of video information
    """
    response.clear()

    try:
        movie = YouTube(URL_PREFIX + movie_id)
        response['info'] = movie.player_config_args['player_response']
    except exceptions.RegexMatchError:
        response['info'] = {'error': 'RegexMatchError Exception :: not valid movie ID'}

    return jsonify(response)


@app.route('/basic_info/<movie_id>')
def get_basic_info(movie_id):
    """
    Get BASIC information of a video based on movie ID
    :param movie_id: the ID of the video
    :return: JSON representation of BASIC video information
    """
    response.clear()

    try:
        movie = YouTube(URL_PREFIX + movie_id)
        title = movie.title
        description = movie.description
        length = movie.length
        views = movie.player_config_args['player_response']['videoDetails']['viewCount']
        rating = movie.player_config_args['player_response']['videoDetails']['averageRating']
        response['title'] = title
        response['description'] = description
        response['length'] = length
        response['views'] = views
        response['rating'] = rating
    except exceptions.RegexMatchError:
        response['info'] = {'error': 'RegexMatchError Exception :: not valid movie ID'}

    return jsonify(response)


@app.route('/streams/<movie_id>')
def get_video_streams(movie_id):
    """
    Get all streams of a video based on movie ID
    :param movie_id: the ID of the video
    :return: JSON representation with video streams
    """
    response.clear()

    try:
        movie = YouTube(URL_PREFIX + movie_id)
        movie_streams = movie.streams.all()

        result = []

        for stream in movie_streams:
            json_resp = {
                'itag': stream.itag,
                'mime_type': stream.mime_type,
                'resolution': stream.resolution,
                'video_codec': stream.video_codec,
                'audio_codec': stream.audio_codec,
                'codecs': stream.codecs,
                # 'fmt_profile': stream.fmt_profile,
                # 'url': stream.url,
                # 'player_config_args': stream.player_config_args
            }
            result.append(json_resp)
        response['info'] = result
    except exceptions.RegexMatchError:
        response['info'] = {'error': 'RegexMatchError Exception :: not valid movie ID'}

    return jsonify(response)


@app.route('/captions/<movie_id>')
def get_video_captions(movie_id):
    """
    Get EN captions of a video based on movie ID
    :param movie_id: the ID of the video
    :return: the caption as string
    """
    try:
        movie = YouTube(URL_PREFIX + movie_id)
        caption_en = movie.captions.get_by_language_code('en')
        caption_en_srt = caption_en.generate_srt_captions()
        result = caption_en_srt

        # Captions: Write to SRT file (uncomment)
        # movie_captions_srt = open('movie_captions_subs.srt', 'w')
        # movie_captions_srt.write(caption_en_srt)
        # movie_captions_srt.close()
    except exceptions.RegexMatchError:
        result = 'RegexMatchError Exception :: not valid movie ID'

    return result


@app.route('/audio/<movie_id>')
def get_only_audio_streams(movie_id):
    """
    Get AUDIO ONLY streams of a video based on movie ID
    :param movie_id: the ID of the video
    :return: JSON representation with AUDIO streams
    """
    response.clear()

    try:
        movie = YouTube(URL_PREFIX + movie_id)
        audio = movie.streams.filter(only_audio=True).all()

        result = []

        for stream in audio:
            resp = {
                'itag': stream.itag,
                'mime_type': stream.mime_type,
                'abr': stream.abr,
                'audio_codec': stream.audio_codec,
                'codecs': stream.codecs,
                'audio_sample_rate': stream.audio_sample_rate,
                'bitrate': stream.bitrate,
                'type': stream.type,
                'subtype': stream.subtype
            }
            result.append(resp)
            response['info'] = result
    except exceptions.RegexMatchError:
        response['info'] = {'error': 'RegexMatchError Exception :: not valid movie ID'}

    return jsonify(response)


@app.route('/download/<movie_id>')
def download_movie(movie_id):
    """
    Download FIRST stream of a video based on movie ID
    :param movie_id: the ID of the video
    :return: JSON representation of response whether file was downloaded or not
    """
    try:
        movie = YouTube(URL_PREFIX + movie_id)
        movie.streams.first().download()
        response['info'] = {'action': 'Downloaded file with id :: ' + movie_id}
    except exceptions.RegexMatchError:
        response['info'] = {'error': 'RegexMatchError Exception :: not valid movie ID'}
    return jsonify(response)


@app.route('/download/<movie_id>/stream_position/<stream_position>')
def download_movie_stream(movie_id, stream_position):
    """
    Download stream of a video from a list of available streams
    based on movie ID and on item position in the list
    :param movie_id: the ID of the video
    :param stream_position: the position of the stream in the list
    :return: JSON representation of response whether file was downloaded or not
    """
    try:
        movie = YouTube(URL_PREFIX + movie_id)
        movie_streams = movie.streams.all()
        movie_streams[int(stream_position)].download()
        response['info'] = {'action': 'Downloaded file with id :: ' + movie_id + ' at position :: ' + stream_position}
    except exceptions.RegexMatchError:
        response['info'] = {'error': 'RegexMatchError Exception :: not valid movie ID'}
    return jsonify(response)


@app.route('/download/<movie_id>/itag/<itag>')
def download_movie_stream_with_itag(movie_id, itag):
    """
    Download stream of a video from a list of available streams
    based on movie ID and movie ITAG
    :param movie_id: the ID of the video
    :param itag: the ITAG of the video
    :return: JSON representation of response whether file was downloaded or not
    """
    try:
        movie = YouTube(URL_PREFIX + movie_id)
        movie_streams = movie.streams.all()

        position_of_stream_with_itag = ""

        for stream in movie_streams:
            if stream.itag == itag:
                position_of_stream_with_itag = str(stream).find(itag)
                break

        movie_streams[position_of_stream_with_itag].download()
        response['info'] = {'action': 'Downloaded file with id :: ' + movie_id + ' and itag :: ' + itag}
    except exceptions.RegexMatchError:
        response['info'] = {'error': 'RegexMatchError Exception :: not valid movie ID'}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
