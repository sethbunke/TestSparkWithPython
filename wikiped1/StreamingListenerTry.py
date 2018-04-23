class StreamingListenerTry(object):

    def __init__(self):
        pass

    def onReceiverStarted(self, receiverStarted):
        """
        Called when a receiver has been started
        """
        pass

    def onReceiverError(self, receiverError):
        """
        Called when a receiver has reported an error
        """
        pass

    def onReceiverStopped(self, receiverStopped):
        """
        Called when a receiver has been stopped
        """
        pass

    def onBatchSubmitted(self, batchSubmitted):
        """
        Called when a batch of jobs has been submitted for processing.
        """
        pass

    def onBatchStarted(self, batchStarted):
        """
        Called when processing of a batch of jobs has started.
        """
        pass

    def onBatchCompleted(self, batchCompleted):
        """
        Called when processing of a batch of jobs has completed.
        """
        pass

    def onOutputOperationStarted(self, outputOperationStarted):
        """
        Called when processing of a job of a batch has started.
        """
        pass

    def onOutputOperationCompleted(self, outputOperationCompleted):
        """
        Called when processing of a job of a batch has completed
        """
        pass