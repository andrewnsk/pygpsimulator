from datetime import datetime


class TimeDate:
    def __init__(self, timezone="local"):
        self._timezone = timezone

    def get_time(self):
        """

        :rtype: time
        """
        if self._timezone == "utc":
            (dt, micro) = datetime.utcnow().strftime('%H%M%S.%f').split('.')
            dt = "%s.%03d" % (dt, int(micro) / 1000)
            return dt
        elif self._timezone == "local":
            (dt, micro) = datetime.now().strftime('%H%M%S.%f').split('.')
            dt = "%s.%03d" % (dt, int(micro) / 1000)
            return dt

    @property
    def get_date(self):
        today = datetime.today()
        return today.strftime('%d%m%y')
