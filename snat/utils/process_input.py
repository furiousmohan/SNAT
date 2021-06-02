from .common_utils import CommonUtils


class ProcessInput(CommonUtils,Interface):

    # Process the input passed by the main controller.
    def process_input(self,input,module):
        if module=='Interface':
            super(Interface).show_options()