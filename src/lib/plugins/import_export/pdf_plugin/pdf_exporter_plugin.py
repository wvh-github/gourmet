from gourmet.plugin import ExporterPlugin
import pdf_exporter
from gettext import gettext as _

PDF = _('PDF (Portable Document Format)')

class PdfExporterPlugin (ExporterPlugin):

    label = _('PDF Export')
    sublabel = _('Exporting recipes to PDF %(file)s.')
    single_completed_string = _('Recipe saved as PDF %(file)s')
    filetype_desc = PDF
    saveas_filters = [PDF,['application/pdf'],['*.pdf']]
    saveas_single_filters = [PDF,['application/pdf'],['*.pdf']]
    mode = 'b'

    def get_multiple_exporter (self, args):
        return pdf_exporter.PdfExporterMultiDoc(args['rd'],
                                                args['rv'],
                                                args['file'],
                                                progress_func=args['prog'],
                                                pdf_args=args['extra_prefs'],
                                                )
    def do_single_exporter (self, args):
        pdf_exporter.PdfExporter(args['rd'],
                                 args['rec'],
                                 args['out'],
                                 change_units=args['change_units'],
                                 mult=args['mult'],
                                 pdf_args=args['extra_prefs'],
                                 )

    def run_extra_prefs_dialog (self):
        return pdf_exporter.get_pdf_prefs()
