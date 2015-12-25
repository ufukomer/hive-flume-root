// Histograms with country traffic values
// @author Omer Ufuk Efendioglu
void htraffic()
{
    const Int_t nc = 9;
    char *country[nc] = {"TR", "SO", "MZ", "JP", "VU", "EG", "QA", "YE", "BO"};

    TCanvas *c1 = new TCanvas("c1","Root Analysis", 10, 10, 900, 500);
    c1 -> SetGrid();
    c1 -> SetTopMargin(0.15);

    TH1F *h = new TH1F("h","Site Traffic By Country", 3, 0, 3);
    h -> SetStats(0);
    h -> SetFillColorAlpha(kAzure-7, 0.35);
    h -> SetBit(TH1::kCanRebin);

    int x;
    char *path_p, *path_s;

    for (int i = 0; i < nc; ++i) {
        ifstream inp;
        char bigString[9];
        char *p = bigString;
        bigString[0] = '\0';

        strcat(p, "data\\");
        strcat(p, country[i]);
        strcat(p, ".dat");

        inp.open(p);

        if (!inp) {
            printf("File open error!\n");
        }

        while (inp >> x) {
            h -> Fill(country[i], x);
        }

        inp.close();
    }

    h -> LabelsDeflate();
    h -> Draw();
}
