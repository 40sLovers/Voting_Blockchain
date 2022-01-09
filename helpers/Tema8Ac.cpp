#include <iostream>
#include<cmath>
using namespace std;
int v[50],w[50],vw[50],vv[50],ww[50],nrbiti,nrbitisuma,nrbitimaxi,pozneg[2];//pozneg pentru a vedea daca numarul rezultat e pozitiv sau negativ
//poz de i=0 la x aiunu si la fel ai si la y
void transformare_baza2p1(int x)
{
    int k=-1,i,j;
    x=abs(x);
    while(x!=0)
    {
        v[++k]=x%2;
        x=x/2;
    }
    if(k+1>nrbiti)
        nrbiti=k+1;
    for(i=0,j=k; i<j; i++,j--)
        swap(v[i],v[j]);
    while(nrbiti>k+1)
    {
        for(i=k; i>=0; i--)
        {
            v[i+1]=v[i];
            v[i]=0;
        }
        k++;
    }

    //for(i=0; i<=k; i++)
    //    cout<<v[i]<<" ";
    //cout<<'\n';
}

void transformare_baza2p2(int y)
{
    int k=-1,i,j;
    y=abs(y);
    while(y!=0)
    {
        w[++k]=y%2;
        y=y/2;
    }
    if(k+1>nrbiti)
        nrbiti=k+1;
    for(i=0,j=k; i<j; i++,j--)
        swap(w[i],w[j]);
    while(nrbiti>k+1)
    {
        for(i=k; i>=0; i--)
        {
            w[i+1]=w[i];
            w[i]=0;
        }
        k++;
    }

    //for(i=0; i<=k; i++)
    //    cout<<w[i]<<" ";
    //cout<<'\n';
}

void transformare_baza2p3(int s)
{
    int k=-1,i,j;
    s=abs(s);
    while(s!=0)
    {
        vw[++k]=s%2;
        s=s/2;
    }
    if(k+1>nrbitisuma)
        nrbitisuma=k+1;
    for(i=0,j=k; i<j; i++,j--)
        swap(vw[i],vw[j]);
    if(nrbiti>nrbitisuma)
        nrbitimaxi=nrbiti;
    else
        nrbitimaxi=nrbitisuma;
    while(nrbitimaxi>k+1)
    {
        for(i=k; i>=0; i--)
        {
            vw[i+1]=vw[i];
            vw[i]=0;
        }
        k++;
    }

    //for(i=0; i<=k; i++)
    //    cout<<vw[i]<<" ";
    //cout<<'\n';
}

int main()
{
    int x,y,op,opfinal,s,pozitivmax,negativmax,nrputere2=1,i;//nr putere pe cat biti se efectueaza operatia
    cin>>x>>y>>op;
    //pentru ms
    if(op==0)
        s=x+y;
    else
        s=x-y;
    if(abs(x)>abs(y))
        while(abs(x)>nrputere2)
            nrputere2*=2;
    else
        while(abs(y)>nrputere2)
            nrputere2*=2;//x nr rezultat care nu trebuie sa depaseasca
    //in urm tinie o sa fac pana la cat poate merge cel mult numarul pentru a nu da eroare
    if(nrputere2>1)
        pozitivmax=nrputere2-1;//x<=2^n-1 la pozitive
    //-2^n-1<=x la negative
    //pentru ms si c1 este formula de mai sus
    //pentru c2 nu trebuie depasit -2^n<=x<=2^n-1
    negativmax=-1*nrputere2-1;
    //cout<<negativmax<<'\n';
    if(abs(x)>abs(y))
    {
        transformare_baza2p1(x);
        transformare_baza2p2(y);
        transformare_baza2p3(s);
    }
    else
    {
        transformare_baza2p2(y);
        transformare_baza2p1(x);
        transformare_baza2p3(s);
    }
    if(x>0)
        cout<<"0 ";
    else
        cout<<"1 ";
    for(i=0; i<=nrbiti-1; i++)//pana la -1 deoarece nr de biti incepe de la 0
        cout<<v[i];
    cout<<'\n';
    if(y>0)
        cout<<"0 ";
    else
        cout<<"1 ";
    for(i=0; i<=nrbiti-1; i++)
        cout<<w[i];
    cout<<'\n';
    cout<<"MS  ";
    if(s>=0)
        cout<<"0 ";
    else
        cout<<"1 ";
    for(i=0; i<=nrbitimaxi-1; i++)
        cout<<vw[i];
    cout<<'\n';
    //cout<<nrbiti<<'\n';
   // cout<<nrbitisuma<<'\n';
    if(nrbitisuma>nrbiti)
        cout<<"eroare depaseste numarul de biti"<<'\n';//pana la MSSSSSSS pana aici...........................................................................
    //pana la MSSSSSSS pana aici..........................................
    //calculeaza bine bitii
    cout<<'\n';
    cout<<"C1"<<'\n'<<'\n'<<'\n';
    //PENTRU C1
    if(op==1)
    {
        y=-1*y;
        op=0;
    }
    for(i=0;i<=nrbiti-1;i++)
    {
        vv[i]=v[i];
        ww[i]=w[i];
    }
    for(i=0;i<=nrbitimaxi-1;i++)
    vw[i]=0;
    //for(i=0;i<=nrbitimaxi;i++)
   //     cout<<vw[i]<< " ";
      if(x<0)
        for(i=0;i<=nrbiti-1;i++)
        v[i]=abs(v[i]-1);
        if(x<0)
            cout<<"1 ";
        else
            cout<<"0 ";
      for(i=0;i<=nrbiti-1;i++)
        cout<<v[i];
        cout<<'\n';
      if(y<0)
        for(i=0;i<=nrbiti-1;i++)
        w[i]=abs(w[i]-1);
        if(y<0)
                cout<<"1 ";
        else
            cout<<"0 ";
      for(i=0;i<=nrbiti-1;i++)
        cout<<w[i];
        cout<<'\n';
        cout<<'\n';
    for(i=0;i<=nrbiti-1;i++)
    {
    vw[i]=v[i]+w[i];
    }
    for(i=nrbiti-1;i>0;i--)
        if(vw[i]>1)
    {
        vw[i]=vw[i]%2;
        vw[i-1]=vw[i-1]+1;
    }
    if(vw[0]>1)
    {
        pozneg[1]=1;
        vw[0]=vw[0]-2;
    }
    if(x<0)
        pozneg[1]++;
    if(y<0)
        pozneg[1]++;
    if(pozneg[1]>1)
    {
        pozneg[0]=1;
        pozneg[1]=pozneg[1]-2;
    }
    if(pozneg[0]==1)
    {
        pozneg[0]=0;
        vw[nrbiti-1]++;
    }
    for(i=nrbiti-1;i>0;i--)
        if(vw[i]>1)
    {
        vw[i]=vw[i]%2;
        vw[i-1]=vw[i-1]+1;
    }
    cout<<pozneg[1]<<" ";
    for(i=0;i<=nrbiti-1;i++)
        cout<<vw[i];
    cout<<'\n';
    if(s>=0&&pozneg[1]==1)
        cout<<"eroare";
        if(s<=0&&pozneg[1]==0)
            cout<<"eroare";
    cout<<'\n'<<'\n';


cout<<"C2"<<'\n'<<'\n';
        //Pentru C2



        for(i=0;i<=nrbitimaxi-1;i++)
        vw[i]=0;
    //for(i=0;i<=nrbitimaxi;i++)
   //     cout<<vw[i]<< " ";
   int ok=0;
      if(x<0)
        for(i=nrbiti-1;i>=0;i--)
        {
            if(vv[i]==1&&ok==0)
            {
                ok=1;
            }
            else if(ok==1)
            {
                vv[i]=abs(vv[i]-1);

            }
        }
        if(x<0)
            cout<<"1 ";
        else
            cout<<"0 ";
      for(i=0;i<=nrbiti-1;i++)
        cout<<vv[i];
        cout<<'\n';
        ok=0;
      if(y<0)
        for(i=nrbiti-1;i>=0;i--)
        {
            if(ww[i]==1&&ok==0)
            {
                ok=1;
            }
            else if(ok==1)
            {
                ww[i]=abs(ww[i]-1);

            }
        }
        if(y<0)
                cout<<"1 ";
        else
            cout<<"0 ";
      for(i=0;i<=nrbiti-1;i++)
        cout<<ww[i];
        cout<<'\n';
        cout<<'\n';


        pozneg[0]=0;
        pozneg[1]=0;

    for(i=0;i<=nrbiti-1;i++)
    {
    vw[i]=vv[i]+ww[i];
    }
    for(i=nrbiti-1;i>0;i--)
        if(vw[i]>1)
    {
        vw[i]=vw[i]%2;
        vw[i-1]=vw[i-1]+1;
    }
    if(vw[0]>1)
    {
        pozneg[1]=1;
        vw[0]=vw[0]-2;
    }
    if(x<0)
        pozneg[1]++;
    if(y<0)
        pozneg[1]++;
    if(pozneg[1]>1)
    {
        pozneg[0]=1;
        pozneg[1]=pozneg[1]-2;
    }
    if(pozneg[0]==1)
    {
        pozneg[0]=0;
    }
    for(i=nrbiti-1;i>0;i--)
        if(vw[i]>1)
    {
        vw[i]=vw[i]%2;
        vw[i-1]=vw[i-1]+1;
    }
    //for(i=0;i<=nrbiti-1;i++)
    //    cout<<vw[i];
        cout<<'\n';




    cout<<pozneg[1]<<" ";
    for(i=0;i<=nrbiti-1;i++)
        cout<<vw[i];
    cout<<'\n';
    if(s>=0&&pozneg[1]==1)
        cout<<"eroare";
        if(s<=0&&pozneg[1]==0)
            cout<<"eroare";
    cout<<'\n'<<'\n';



        /*for(i=0;i<=nrbitimaxi;i++)
    vw[i]=0;
    for(i=0;i<=nrbitimaxi;i++)
        cout<<vw[i]<< " ";*/
    return 0;
}
