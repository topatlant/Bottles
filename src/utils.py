# utils.py
#
# Copyright 2020 brombinmirko <send@mirko.pm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging, socket

'''
Set the default logging level
'''
logging.basicConfig(level=logging.DEBUG)

class UtilsConnection():

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)

        self.window = window

    def check_connection(self, show_notification=False):
        try:
            socket.create_connection(("1.1.1.1", 53))
            logging.info("Connection status: online …")
            self.window.toggle_btn_noconnection(False)
            return True
        except OSError:
            logging.info("Connection status: offline …")
            self.window.toggle_btn_noconnection(True)

            if show_notification:
                self.window.send_notification("Bottles",
                                              "You are offline, unable to download.",
                                              "network-wireless-disabled-symbolic")
            pass
        return False
