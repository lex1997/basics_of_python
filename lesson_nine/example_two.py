from example_one import OwnerPrint
import datetime

time_now = datetime.datetime.now()

st = OwnerPrint(str(time_now))
st.uppercase()
