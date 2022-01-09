#include <iostream>
#include<bitset>
#include<cmath>
using namespace std;
int v[50],c1[50],c2[50],w[50];
void parte_fractionara(float x,int b)
{
    int i;
    //x=x-int(x);
    for(i=1; i<=20&&x!=0; i++)
    {
        v[i]=abs(int(x*b));
        x=x*b-int(x*b);
    }
    --i;
    //for(int k=1; k<=i; k++)
    //    if (v[k] <= 9)
    //       cout << v[k];
}


//numerele sunt 00000000000010010
void deplasare_numere_pozitiveMS(int exponent2,int nrbiti)
{
    int i;
    if(exponent2>0)
    {
        for(i=0; i<=nrbiti-1; i++)
        {
            v[i-exponent2]=v[i];
            v[i]=0;
        }
    }
    else
    {
        if(exponent2<0) // la acesta exponent2 are deja minus si daca ii punem inca unu in fata devine +
            for(i=nrbiti-1; i>=0; i--)
            {
                v[i-exponent2]=v[i];
                v[i]=0;
            }
    }
}
void deplasare_numere_pozitiveC1(int exponent2,int nrbiti)
{
    int i;
    if(exponent2>0)
    {
        for(i=0; i<=nrbiti-1; i++)
        {
            c1[i-exponent2]=c1[i];
            c1[i]=1;
        }
    }
    else
    {
        if(exponent2<0) // la acesta exponent2 are deja minus si daca ii punem inca unu in fata devine +
            for(i=nrbiti-1; i>=0; i--)
            {
                c1[i-exponent2]=v[i];
                c1[i]=1;
            }
    }

}

void  deplasare_numere_pozitiveC2(int exponent2,int nrbiti)
{
       int i;
    if(exponent2>0)
    {
        for(i=0; i<=nrbiti-1; i++)
        {
            c2[i-exponent2]=c1[i];
            c2[i]=1;
        }
    }
    else
    {
        if(exponent2<0) // la acesta exponent2 are deja minus si daca ii punem inca unu in fata devine +
            for(i=nrbiti-1; i>=0; i--)
            {
                c2[i-exponent2]=v[i];
                c2[i]=0;
            }
    }
}

int main()
{
    float n;
    int nrbiti,i,k=-1,nn,j,exponent2;
    cin>>n>>nrbiti; // daca avem numere fractionare le facem manual
    cin>>exponent2;//2^nrputere
    if(int(n)==n)//verific daca n este intreg daca daca se face
    {
        nn=abs(int(n));
        while(nn!=0)
        {
            v[++k]=nn%2;
            nn=nn/2;
        }
        // if(n>=0)
        //     cout<<0<<" ";
        // else
        //     cout<<1<<" ";
        for(i=nrbiti-1,j=0; i>j; i--,j++) //am bitii de la stanga la dreapta de aia afisez invers
            swap(v[i],v[j]);
        // for(i=0;i<=nrbiti-1;i++)
        //       cout<<v[i];
    }
    else
    {

        parte_fractionara(n,2);

    }
    for(i=0; i<=nrbiti-1; i++)
        cout<<v[i];
    cout<<'\n';
    if(n>=0)
    {
        deplasare_numere_pozitiveMS(exponent2,nrbiti);
        cout<<0<<" ";
    for(i=0; i<=nrbiti-1; i++)
        cout<<v[i];
        }
    else        //pentru negative
     {
         cout<<"pentru ms  "<<1<<" ";
         deplasare_numere_pozitiveMS(exponent2,nrbiti);
        for(i=0; i<=nrbiti-1; i++)
        cout<<v[i];
        cout<<'\n';
        cout<<"pentru c1  "<<1<<" ";
         for(i=0;i<=nrbiti-1;i++)
            cout<<abs(v[i]-1);
         cout<<'\n';
         cout<<"pentru c2 "<<1<<" ";
         int ok=0;
        for(i=nrbiti-1; i>=0; i--)//pentru c2 o sa fac un alt vector deoarece le pun invers
        {
            if(v[i]==1&&ok==0)
            {
                ok=1;
                w[i]=v[i];
            }
            else if(ok==1)
            {
                w[i]=abs(v[i]-1);

            }
            else
                w[i]=v[i];
        }
        for(i=0;i<=nrbiti-1;i++)
            cout<<w[i];
    }
    return 0;
}
