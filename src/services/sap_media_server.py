import os
import sap_media_api


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    sap_media_api.app.run(host='127.0.0.1', port=port)