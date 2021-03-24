import subprocess
import PySimpleGUI as sg


class UI():
    my_new_theme = {'BACKGROUND': '#709053',
                    'TEXT': '#fff4c9',
                    'INPUT': '#c7e78b',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('white', '#709053'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}

    def __init__(self):
        # the app window
        self.appName = 'OMEGA-DMCA-LUL'
        self.windowColor = sg.theme('DefaultNoMoreNagging')
        self.layout = [
            [sg.Button(image_filename=r'assets\FMAsymbole.png'),
                       sg.T('Chose song/playlist URL', key='input')],
                        [sg.In('', key='url',)],
                        [sg.Button(image_filename=r'assets\addURL.png',
                                   key='Confirm URL', ),
                         sg.Button(image_filename=r'assets\reset.png',
                                   key='Clear URL', size=(125, 38))
                         ],
                        [sg.Button('Cancel')],
                        [sg.Output(size=(88, 20), key='output')],
                        [sg.Button(image_filename=r'assets\firstButton.png',
                                   key='download')
                         ],
                        [sg.Button('auto Gen subtitles')],
                        [sg.Button('Version checker')],
                        [sg.Button('help')]
        ]
        self.event = ''
        self.values = ''
        self.startDownload = None
        self.link = None
        self.activeWindow = sg.Window(self.appName, self.layout)
    # app state and events handler

    def test(self):
        self.currentData = []
        while not self.event == 'Cancel':
            self.event, self.values = self.activeWindow.read()
            self.currentData = self.buttonFunction(self.event)
            if self.currentData:
                print('current command: ', ' '.join(self.currentData))
        self.activeWindow.close()
    # button functions

    def buttonFunction(self, button):
        argList = ['youtube-dl', '-i', '-h', '--yes-playlist',
                   self.values['url'], self.event, self.currentData,
                   '--version', '--write-auto-sub', '--skip-download', '--sub-format best']
        eventButtons = {'Confirm URL': [argList[0], argList[1], argList[3], argList[4]],
                        'Clear URL': '',
                        'download': argList[6],
                        'help': [argList[0], argList[2]],
                        'Cancel': argList[5],
                        'Version checker': [argList[0], argList[7]],
                        'auto Gen subtitles': [argList[0], argList[8], argList[4], argList[9]]}

        if button == 'download':
            self.currentData = eventButtons[button]
            self.download()
        else:
            return eventButtons[button]

    # the download handler
    def download(self):

        layout = [[sg.Text('download')],
                [sg.ProgressBar(1, orientation='h', size=(
                    20, 20), key='progress')],
                [sg.Cancel()]]

        # create the form`
        with  subprocess.Popen(self.currentData, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT) as run:
            window = sg.Window('Custom Progress Meter', layout)
            progress_bar = window['progress']
            # loop that would normally do something useful
            i = 0
            for line0 in iter(run.stdout.readline, b''):

                # check to see if the cancel button was clicked and exit loop if clicked
                event, values = window.read(timeout=0)
                if event == 'Cancel' or event == None:
                    break
                    # update bar with loop value +1 so that bar eventually reaches the maximum
                print('>>> ' + str(line0, 'utf-8'))
                progress_bar.update_bar(i+1, 10)

                
                # done with loop... need to destroy the window as it's still open
        window.close()
        
        
            
UI().test()
