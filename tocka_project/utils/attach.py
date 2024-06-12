import allure
from allure_commons.types import AttachmentType
from requests import Response
import logging
import json

def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body.decode('utf-8'))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)

def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body.decode('utf-8'), indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )

def add_screenshot(browser):
    png = browser.get_screenshot_as_png()  # Убираем `.driver`
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

def add_logs(browser):
    if browser.capabilities['browserName'] == 'chrome':  # Убираем `.driver`
        log = "".join(f'{text}\n' for text in browser.get_log(log_type='browser'))  # Убираем `.driver`
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

def add_html(browser):
    html = browser.page_source  # Убираем `.driver`
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.session_id + ".mp4"  # Убираем `.driver`
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.session_id, AttachmentType.HTML, '.html')
