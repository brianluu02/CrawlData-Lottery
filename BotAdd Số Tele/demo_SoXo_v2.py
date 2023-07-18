import logging
import io
import datetime
import pandas as pd
from telegram import Update, ForceReply
from telegram.ext import (Updater, CommandHandler, CallbackContext)
import numpy as np
import csv

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    start_text = """
    Chào bạn! Tôi là bot giúp bạn xem giá Bitcoin và các đồng tiền mã hóa khác.
    Nếu bạn muốn làm giàu trong mơ thì suy nghĩ thêm con bot tôi trả lời nhá :v
    Cách sử dụng:
    /start - Bắt đầu trò chuyện với bot
    /help - Hiển thị thông tin trợ giúp bạn khi chưa biết lấy API của 1 Coin nào đó 
    /price - Hiển thị giá Bitcoin (mặc định) hoặc giá của một đồng tiền cụ thể khi được chỉ định
    Ví dụ như /price tether
    """
    update.message.reply_text(start_text)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message with an image when the command /help is issued."""
    help_text = """
    Các bước lấy API :
    B1: Truy cập trang websites sau --> https://www.coingecko.com
    B2: Tìm đồng Coin muốn mua hoặc kham khảo giá vv... và nhấp vào đồng tiền đã chọn 
    B3: Làm theo hình ảnh minh họa bên dưới lấy API đồng tiền 
    B4: Ví dụ như /price tether
    Lưu ý: Mỗi Coin là API khác nhau 
    """
    # Đường dẫn tới ảnh trên internet
    image_url = "https://upanh.tv/image/iASRDA"
    # Gửi thông điệp văn bản
    update.message.reply_text(help_text)
    
    # Gửi ảnh từ URL
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)




# added_SoXo = []

# def add_SoXo(update: Update, context: CallbackContext) -> None:
#     """Add new lottery numbers."""
#     so_xo_list = update.message.text.split(' ')[1:]  # Get the list of lottery numbers from the message
    
#     if len(so_xo_list) > 6:
#             update.message.reply_text("Vui lòng chỉ nhập tối đa 6 số xổ.")
#     return

#     for number in so_xo_list:
#         if len(number) == 2:
#             Giai_7([number])  # Save two-digit numbers to the TwoDigit_Numbers.csv file
#         elif len(number) == 3:
#             Giai_6([number])  # Save three-digit numbers to the ThreeDigit_Numbers.csv file
#         elif len(number) == 4:
#             Giai_4([number]) 
#         elif len(number) == 5:
#             Giai_3([number]) 
#     update.message.reply_text("Các số xổ đã được thêm thành công.")



def add_SoXo(update: Update, context: CallbackContext) -> None:
    """Add new lottery numbers."""
    so_xo_list = update.message.text.split(' ')[1:]  # Get the list of lottery numbers from the message

    # if len(so_xo_list) != 5:
    #     update.message.reply_text("Vui lòng chỉ nhập tối đa 5 số xổ.")
    #     return

    for number in so_xo_list:
        if len(number) == 2:
            Giai_7([number])  # Save two-digit numbers to the TwoDigit_Numbers.csv file
        elif len(number) == 3:
            Giai_6([number])  # Save three-digit numbers to the ThreeDigit_Numbers.csv file
        elif len(number) == 4:
            Giai_4([number])
        elif len(number) == 5:
            Giai_3([number])
    
    update.message.reply_text("Các số xổ đã được thêm thành công.")


def Giai_7(numbers):
    """Save two-digit numbers to a CSV file."""
    with open('./Giai_7.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)

def Giai_6(numbers):
    """Save three-digit numbers to a CSV file."""
    with open('./Giai_6.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)

def Giai_4(numbers):
    """Save three-digit numbers to a CSV file."""
    with open('./Giai_4.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)
def Giai_3(numbers):
    """Save three-digit numbers to a CSV file."""
    with open('./Giai_3.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)   

def load_SoXo():
    """Load the list of added cryptocurrencies from a CSV file."""
    try:
        with open('./XSMB_7.csv', 'r') as file:
            reader = csv.reader(file)
            SoXo = next(reader)
            return SoXo
    except FileNotFoundError:
        return []
    

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("API TeleGram ")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("add", add_SoXo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
if __name__ == "__main__":
    main()
#  bài hoàn chỉnh nhất 
