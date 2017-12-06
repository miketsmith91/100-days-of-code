import SongLink
import youtube_dl
import SheetService

# class SongConverter(object):
#     def __init__(self, currentSongLink):
#         self.currentSongLink = SongLink.SongLink(currentSongLink)


inProgressRange = 'In Progress!A2:E'

def video_to_audio(songLink,googleSheet):
    options = {
        # Changed to only bestaudio because i'm skeptical. 'format': 'bestaudio/best', # choice of quality
        'format': 'bestaudio',
        'extractaudio': True,  # only keep the audio. No video needed.
        'audioformat': "mp3",  # convert to mp3
        'outtmpl': songLink.get__youtube_dl_Output_Name() + '.%(ext)s',  # name the file the ID of the video
        # 'outtmpl': '%(title)s' + '.%(ext)s',  # name the file the ID of the video
        'noplaylist': True, }  # only download single song, not playlist
    try:
        ydl = youtube_dl.YoutubeDL(options)

        result = ydl.extract_info(songLink.get__url(), download=True)
    except Exception as err:
        print ("An exception just occurred bro!: " + str(err))
        # row[4] = err
        exception = 'Invalid Link'
        # addToErrorSpreadsheet(row,rowNumber,exception,err)
        googleSheet.addToErrorSpreadsheet(row, rowNumber, exception, err)
        # values = getInProgressSpreadSheet()
        values = googleSheet.getSpreadsheet(inProgressRange)

        continue
    print(result.get('title'))

    songFileName = youtube_dl_Output_Name + "." + result.get('ext')


if not values:
    print('No data found.')
else:
    print('Link, Song Artist, Song Name:')
    rowNumber = 2
    for row in values:
        try:

            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s, %s' % (row[0], row[1], row[2]))
            songLink = row[0]
            songArtist = row[1]
            songName = row[2]
            youtube_dl_Output_Name = songArtist + " - " + songName
        except Exception as err:
            print ("An exception just occured dude!: " + str(err))
            exception = "Empty Non-optional Values"
            # addToErrorSpreadsheet(row,rowNumber,exception,err)
            GoogleSheet.addToErrorSpreadsheet(row, rowNumber, exception, err)
            # values = getInProgressSpreadSheet()
            values = GoogleSheet.getSpreadsheet(inProgressRange)
            continue
        options = {
            # Changed to only bestaudio because i'm skeptical. 'format': 'bestaudio/best', # choice of quality
            'format': 'bestaudio',
            'extractaudio': True,  # only keep the audio. No video needed.
            'audioformat': "mp3",  # convert to mp3
            'outtmpl': youtube_dl_Output_Name + '.%(ext)s',  # name the file the ID of the video
            # 'outtmpl': '%(title)s' + '.%(ext)s',  # name the file the ID of the video
            'noplaylist': True, }  # only download single song, not playlist

        try:

            ydl = youtube_dl.YoutubeDL(options)

            result = ydl.extract_info(songLink, download=True)

        except Exception as err:
            print ("An exception just occurred bro!: " + str(err))
            # row[4] = err
            exception = 'Invalid Link'
            # addToErrorSpreadsheet(row,rowNumber,exception,err)
            GoogleSheet.addToErrorSpreadsheet(row, rowNumber, exception, err)
            # values = getInProgressSpreadSheet()
            values = GoogleSheet.getSpreadsheet(inProgressRange)

            continue

        print(result.get('title'))

        songFileName = youtube_dl_Output_Name + "." + result.get('ext')