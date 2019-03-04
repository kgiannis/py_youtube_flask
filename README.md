# py_youtube_flask
A sample project in Python using pyTube and Flask

# Installation
Use pip to install pyTube
```sh
$ pip install pytube
```

# Usage
There are eight endpoints available in order to demonstrate the usage of the **pyTube** library.
Test each endpoint on http://localhost:5000 by default (Flask) 


### Basic information endpoints

**Endpoint:** /<movie_id>
**Info:** Get information of the video, e.g playabilityStatus, videoDetails etc.
**Example Response:** 
```
"info": {
"playabilityStatus": {
"status": "OK",
"playableInEmbed": true
}
```

**Endpoint:** /basic_info/<movie_id>
**Info:** Get information of the video for title, description, length, views, rating
**Example Response:**
```
{
"title": "ALADDIN Trailer 2 (2019)",
"description": "New trailer for Aladdin",
"length": "159",
"views": "12460070",
"rating": 3.6985295
}
```

**Endpoint:** /streams/<movie_id>
**Info:** Get information of the available video streams. 
**Example Response:*
```
{
"info": [
{
"itag": "22",
"mime_type": "video/mp4",
"resolution": "720p",
"video_codec": "avc1.64001F",
"audio_codec": "mp4a.40.2",
"codecs": [
"avc1.64001F",
"mp4a.40.2"
]
},
{
"itag": "43",
"mime_type": "video/webm",
"resolution": "360p",
"video_codec": "vp8.0",
"audio_codec": "vorbis",
"codecs": [
"vp8.0",
"vorbis"
]
},
```

**Endpoint:** /captions/<movie_id>
**Info:** Get the EN captions if any. You can also uncomment the part of the code where you can download the captions as .srt file

**Endpoint:** /audio/<movie_id>
**Info:** Get all the available audio streams of the video
**Example Response:**
```
{
"info": [
{
"itag": "140",
"mime_type": "audio/mp4",
"abr": "128kbps",
"audio_codec": "mp4a.40.2",
"codecs": [
"mp4a.40.2"
],
"audio_sample_rate": "44100",
"bitrate": "130478",
"type": "audio",
"subtype": "mp4"
},
```


### Stream downloading endpoints

**Endpoint:** /download/<movie_id>
**Info:** Download the FIRST stream from the available video streams

**Endpoint:** /download/<movie_id>/stream_position/<stream_position>
**Info:** From the list of the available video streams download the one in the specified list position (stream_position)


**Endpoint:** /download/<movie_id>/itag/<itag>
**Info:** Download the stream with the specified ITAG from the list of streams

