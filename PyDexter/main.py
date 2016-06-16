import os
import webbrowser

class PyDexter:
    def __init__(self, config = {}):
        self.config = config

    def configure(self, config):
        self.config = config

    def timeline(self, config):
        self._launch_chart('timeline', config)

    def bar(self, config):
        self._launch_chart('bar', config)

    def hist(self, config):
        return self._launch_chart('hist', config)

    def pie(self, config):
        self._launch_chart('pie', config)

    def plot(self, config):
        self._launch_chart('plot', config)

    def scatter(self, x1, x2 = None):
        if x2 is None:
            dataset = { 'x': list(range(len(x1))), 'y': x1 }
        else:
            dataset = { 'x': x1, 'y': x2 }

        self.plot({ 'datasets': [dataset] })

    def _launch_chart(self, chart_type, config):
        js = self._make_js(chart_type, config)
        html = self._html_head() + js + self._html_tail()
        path = self._write_file(html)
        self._open_file(path)

    def _make_js(self, chart_type, config):
        js = "new D3xter({0}).{1}({2}); \n".format(
          self.config,
          chart_type,
          config
        )
        return js

    def _html_head(self):
        head = """
        <html>
          <head>
            <script src="bower_components/d3/d3.js" charset="utf-8"></script>
            <link rel="stylesheet" href="bower_components/d3xter/css/style.css">
            <script src="bower_components/d3xter/js/lib.js" charset="utf-8"></script>
          </head>
          <body>
            <script type="text/javascript">
        """
        return head

    def _html_tail(self):
        tail = """
            </script>
          </body>
        </html>
        """
        return tail

    def _write_file(self, html, path = None):
        if path is None: path = "./pydex_plot.html"
        f = open(path, 'w')
        f.write(html)
        f.close()

        return path

    def _open_file(self, path):
        absolute_path = os.path.realpath(path)
        webbrowser.open('file://' + absolute_path)
