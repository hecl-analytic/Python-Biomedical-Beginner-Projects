raw_log = """
2024-01-21 10:00:00 | PID: 101 | HR: 72 | ST: Normal
2024-01-21 10:05:00 | PID: 102 | HR: 85 | ST: Normal
2024-01-21 10:10:00 | PID: 103 | HR: error | ST: Sensor Fail
2024-01-21 10:15:00 | PID: 101 | HR: 160 | ST: TACHYCARDIA
2024-01-21 10:20:00 | PID: 104 | HR: 45 | ST: Bradycardia
"""

def parse_log(log_data:list):
    measurement = []
    convert = log_data.strip().split("\n")
    for i in convert:
        convert_row = i.strip().split("|")

        geting_pid = convert_row[1].strip().split(":")
        pid = geting_pid[1].strip()

        raw_hr = convert_row[2].strip().split(":")
        hr = raw_hr[1].strip()

        if hr == "error":
            continue

        geting_status = convert_row[3].strip().split(":")
        status = geting_status[1]

        single_measurement = {
            "pid":int(pid),
            "hr":int(hr),
            "status": status
        }
        measurement.append(single_measurement)
    return measurement
meas = parse_log(raw_log)
print(meas)