from pygpsimulator import simutime


class PositionData:
    """
    Class that represents simulation of navigation data of NMEA 0183 (GPS uses WGS84 Datum)
    Use current system time (local time zone), as UTC GPS time.

    :parameter system_id: GPS (GP) or GLONASS (GL). Default is GP
    :type system_id: Unicode
    :parameter sentence_id: Sentence Identifier, RMC, GGA etc. Default is RMC (recommended minimum sentence)
    :parameter status: validity  A - valid, V - invalid. Default is valid
    :parameter latitude: the location's latitude. Must be between 0 and 90
    :parameter ns: type of latitude - North/South - N or S
    :parameter longitude: the location's longitude. Must be between 0 and 180
    :parameter ew: type of longitude - East/West - E or W
    :parameter speed: speed in knots
    :parameter course: true course in degrees
    :parameter variation: in degrees
    :parameter variation_ew: type of variation - East/West - E or W
    :parameter mode: A -  autonomous, D - differential, E - approximation, N - unreliable
    :parameter fixquality: 0 - invalid, 1 - GPS fix, 2 - DGPS fix. Default GPS fix - 1
    :parameter satellites: number of satellites
    :parameter hdop: Horizontal Dilution of Precision (HDOP), Relative accuracy of horizontal position
    :parameter hog: Height of geoid above WGS84 ellipsoid
    :parameter tslu: Time since last DGPS update
    :parameter dgps_station_id: DGPS reference station id

    """

    def __init__(self, system_id='GP',
                 sentence_id='RMC',
                 status='A',
                 latitude='4001.20676',
                 ns='N',
                 longitude='10512.97088',
                 ew='W',
                 speed='0.06',
                 course='25.82',
                 variation='',
                 variation_ew='',
                 mode='D',
                 fixquality='1',
                 satellites='07',
                 hdop='',
                 altitude='150.0',
                 hog='',
                 tslu='',
                 dgps_station_id=''):
        self._system_id = system_id
        self._sentence_id = sentence_id
        self._status = status
        self._latitude = latitude
        self._ns = ns
        self._longitude = longitude
        self._ew = ew
        self._speed = speed
        self._course = course
        self._variation = variation
        self._variation_ew = variation_ew
        self._mode = mode
        self._fixquality = fixquality
        self._satellites = satellites
        self._hdop = hdop
        self._altitude = altitude
        self._hog = hog
        self._tslu = tslu
        self._dgps_station_id = dgps_station_id

    def get_coord(self):
        if self._sentence_id == "RMC":
            return "{0}{1},{2},{3},{4},{5},{6},{7}," \
                   "{8},{9},{10},{11},{12},{13}".format(self._system_id, self._sentence_id,
                                                        simutime.TimeDate().get_time(), self._status,
                                                        self._latitude, self._ns, self._longitude, self._ew,
                                                        self._speed, self._course, simutime.TimeDate().get_date,
                                                        self._variation, self._variation_ew, self._mode)
        elif self._sentence_id == "GGA":
            return "{0}{1},{2},{3},{4},{5},{6},{7}," \
                   "{8},{9},{10},M,{11},M,{12},{13}".format(self._system_id, self._sentence_id,
                                                            simutime.TimeDate().get_time(),
                                                            self._latitude, self._ns, self._longitude, self._ew,
                                                            self._fixquality, self._satellites, self._hdop,
                                                            self._altitude, self._hog, self._tslu,
                                                            self._dgps_station_id)

        else:
            return "Unknown sentence"

    def checksum(self):
        cksum = 0
        data = self.get_coord()
        for ch in str(data):
            cksum ^= ord(ch)
        return '$' + data + '*%02X\r\n' % cksum
