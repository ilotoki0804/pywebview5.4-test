from __future__ import annotations

import webview

class Api:
    def hello(self):
        print('Hello, world!')

if __name__ == '__main__':
    api = Api()
    main_window = webview.create_window('main', 'assets/index.html', js_api=api, min_size=(600, 450))
    webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False
    webview.start(func=api.hello, ssl=True)
