if __name__ == "__main__":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(0)

        from vrct_gui.splash_window import SplashWindow
        splash = SplashWindow()
        splash.showSplash()

        from config import config
        from models.translation.utils import downloadCTranslate2Weight
        if config.USE_TRANSLATION_FEATURE is True:
            downloadCTranslate2Weight(config.PATH_LOCAL, config.CTRANSLATE2_WEIGHT_TYPE, splash.updateDownloadProgress)
        splash.toProgress(0)

        # whisperのダウンロードの説明に変更する必要あり
        if config.USE_WHISPER_FEATURE is True:
            from models.transcription.transcription_whisper import downloadWhisperWeight
            downloadWhisperWeight(config.PATH_LOCAL, config.WHISPER_WEIGHT_TYPE, splash.updateDownloadProgress)
        splash.toProgress(0)

        import controller
        controller.createMainWindow(splash)
        splash.destroySplash()
        controller.showMainWindow()

    except Exception:
        import traceback
        with open('error.log', 'a') as f:
            traceback.print_exc(file=f)