using System;
using DinkToPdf;
namespace pdf_from_html
{
    class Program
    {
        static void Main(string[] args)
        {
            string finalHTMLVersion = System.IO.File.ReadAllText("C:\\Users\\alex.gusatu\\Desktop\\index.html");
            var pdfFromHTML = ConvertHTMLToPdfClass.ConvertHTMLToPdf(finalHTMLVersion);
            System.IO.File.WriteAllBytes("C:\\Users\\alex.gusatu\\Desktop\\aici.pdf", pdfFromHTML);
        }
    }
}
public class ConvertHTMLToPdfClass
{
    public static BasicConverter converter = new SynchronizedConverter(new PdfTools());
    public static byte[] ConvertHTMLToPdf(string finalHTMLVersion)
    {
        //_converter = new BasicConverter(new PdfTools());
        var doc = new HtmlToPdfDocument()
        {
            GlobalSettings = {
                            ColorMode = ColorMode.Color,
                             Orientation = Orientation.Portrait,
                            PaperSize = PaperKind.A4,
                        },
            Objects = {
                             new ObjectSettings() {
                                HtmlContent = finalHTMLVersion,
                                WebSettings = { DefaultEncoding = "utf-8" ,
                                     UserStyleSheet = ""},

                            }
                        }
        };

        var pdfdoc = converter.Convert(doc);
        return pdfdoc;
    }

}