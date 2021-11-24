#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;
#define w 640
#define h 480
char buf[2000000] = {0};
void WriteBMP(char *img, const char *filename)
{
    int l = (w * 3 + 3) / 4 * 4;
    int bmi[] = {l * h + 54, 0, 54, 40, w, h, 1 | 3 * 8 << 16, 0, l * h, 0, 0, 100, 0};
    FILE *fp = fopen(filename, "wb");
    fprintf(fp, "BM");
    fwrite(&bmi, 52, 1, fp);
    fwrite(img, 1, l * h, fp);
    fclose(fp);
}
int main()
{
    int j = 0;
    char img[w * h * 3];
    ifstream fin;
    char file[40] = "../data/1.rgb32";
    cin >> file;
    fin.open(file, std::ios::binary);
    if (!fin)
    {
        std::cerr << "cannot open the file";
    }
    fin.read(buf, sizeof(char) * 2000000);
    for (int i = 0; i < w * h * 3; i++)
    {
        if ((j + 1) % 4 == 0)
            j++;
        img[i] = buf[j];
        j++;
    }
    //   img[i] = rand() % 256;
    char file2[40] = "test.bmp";
    cin >> file2;
    WriteBMP(img, file2);
    return 0;
}
