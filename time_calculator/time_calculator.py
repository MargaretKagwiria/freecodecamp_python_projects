def add_time(start, duration, day=None):
  days_week = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6}
  start_time, mid_day = start.split()
  start_hour, start_minute = start_time.split(':')
  hours = int(start_hour)
  minutes = int(start_minute)

  if mid_day == 'PM':
    hours += 12

  dur_hour, dur_minute = duration.split(':')
  add_hours = int(dur_hour)
  add_minutes = int(dur_minute)
  tot_minutes = minutes + add_minutes
  rem_minutes = tot_minutes % 60
  rem_hours = tot_minutes // 60
  tot_hours = hours + add_hours + rem_hours
  final_hours = (tot_hours % 24) % 12

  if final_hours == 0:
    final_hours = 12

  num_days = tot_hours // 24

  val_mid_day = None
  if (tot_hours % 24) <= 11:
    val_mid_day = "AM"
  else:
    val_mid_day = "PM"

  if rem_minutes <= 9:
    rem_minutes = '0' + str(rem_minutes)
  else:
    rem_minutes = str(rem_minutes)

  final_time = str(final_hours) + ':' + rem_minutes + ' ' + val_mid_day
  new_time = None
  if day == None:
    if num_days == 0:
      new_time = final_time
    if num_days == 1:
      new_time = final_time + ' (next day)'
    if num_days > 1:
      new_time = final_time + ' ('+ str(num_days) +' days later)'
  else:
    final_day = (days_week[day.lower().capitalize()] + num_days) % 7
    for d, k in days_week.items():
      if k == final_day:
        final_day = d
        break
    if num_days == 0:
      new_time = final_time + ',' + ' ' + final_day
    if num_days == 1:
     new_time = final_time + ',' + ' ' + final_day + ' (next day)'
    if num_days > 1:
      new_time = final_time + ',' + ' ' + final_day + ' ('+ str(num_days) +' days later)'
    
  return new_time