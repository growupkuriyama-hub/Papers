// Usage: sub words.txt d k P [ceilchars]
// type = (window_k of each comp: exact if len<2k else pref_k,suf_k) x (contains any ceilchar)
#include <bits/stdc++.h>
using namespace std; typedef unsigned long long u64; typedef __uint128_t u128;
static const u64 MOD=(1ULL<<61)-1; u64 B=1000003ULL*7919+12345;
u64 mulm(u64 a,u64 b){u128 c=(u128)a*b; u64 lo=(u64)(c&MOD), hi=(u64)(c>>61); u64 r=lo+hi; if(r>=MOD) r-=MOD; return r;}
u64 mix(u64 x){x+=0x9e3779b97f4a7c15ULL; x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL; x=(x^(x>>27))*0x94d049bb133111ebULL; return x^(x>>31);}
vector<string> W; int D,K,P; string CEIL="<>";
struct WS{ vector<u64> h,pw; vector<int> c; };
vector<WS> pre;
inline u64 sub(const WS&s,int i,int j){ u64 v=(s.h[j]+MOD-mulm(s.h[i],s.pw[j-i]))%MOD; return mix(v*1315423911ULL+ (u64)(j-i)); }
inline u64 typeOf(const WS&s,int i,int j){ int L=j-i; u64 t; if(L<2*K) t=sub(s,i,j); else t=mix(sub(s,i,i+K)*31+sub(s,j-K,j)); bool z=(s.c[j]-s.c[i])>0; return mix(t+ (z?7:3)); }
int main(int argc,char**argv){
  ifstream f(argv[1]); string line; while(getline(f,line)) if(!line.empty()) W.push_back(line);
  D=atoi(argv[2]); K=atoi(argv[3]); P=atoi(argv[4]); if(argc>5) CEIL=argv[5];
  for(auto&w:W){ WS s; int n=w.size(); s.h.assign(n+1,0); s.pw.assign(n+1,1); s.c.assign(n+1,0);
    for(int i=0;i<n;i++){ s.h[i+1]=(mulm(s.h[i],B)+(unsigned char)w[i])%MOD; s.pw[i+1]=mulm(s.pw[i],B); s.c[i+1]=s.c[i]+(CEIL.find(w[i])!=string::npos);} pre.push_back(s);}
  unordered_map<u64,u64> setH; setH.reserve(1<<24);
  long long occ=0;
  vector<int> cut(2*D);
  // enumerate cuts recursively
  auto forEach=[&](auto&& fn){
    for(size_t wi=0;wi<W.size();wi++){ const WS&s=pre[wi]; int n=W[wi].size();
      // iterative combination of 2D strictly increasing positions in [0,n]
      int m=2*D; if(m>n+1) continue; for(int i=0;i<m;i++) cut[i]=i;
      while(true){ fn(s,n);
        int i=m-1; while(i>=0 && cut[i]==n-(m-1-i)) i--; if(i<0) break; cut[i]++; for(int j=i+1;j<m;j++) cut[j]=cut[j-1]+1; }
    }};
  auto keys=[&](const WS&s,int n,u64&tk,u64&ck,u64&ty){
    tk=0x1234; ck=0x5678; ty=0x9abc;
    for(int j=0;j<D;j++){ tk=mix(tk*1000003ULL+sub(s,cut[2*j],cut[2*j+1])); ty=mix(ty*998244353ULL+typeOf(s,cut[2*j],cut[2*j+1])); }
    ck=mix(ck+sub(s,0,cut[0]));
    for(int j=0;j<D-1;j++) ck=mix(ck*1000003ULL+sub(s,cut[2*j+1],cut[2*j+2]));
    ck=mix(ck*1000003ULL+sub(s,cut[2*D-1],n)); };
  forEach([&](const WS&s,int n){ u64 tk,ck,ty; keys(s,n,tk,ck,ty); setH[tk]+=mix(ck); occ++; });
  fprintf(stderr,"occurrences %lld distinct tuples %zu\n",occ,setH.size());
  long long viol=0;
  for(int p=0;p<P;p++){ unordered_map<u64,pair<u64,pair<int,vector<int>>>> m2; m2.reserve(1<<22); static int curw=0;
    forEach([&](const WS&s,int n){ u64 tk,ck,ty; keys(s,n,tk,ck,ty); if(ck%P!=(u64)p) return; u64 key=mix(ck^mix(ty)); u64 sh=setH[tk];
      int wi=&s-&pre[0]; auto it=m2.find(key); if(it==m2.end()) m2.emplace(key,make_pair(sh,make_pair(wi,cut))); else if(it->second.first!=sh){ if(viol<4){ auto pr=[&](int w,const vector<int>&c){ const string&S=W[w]; fprintf(stderr,"  word %s  ctx(%s|",S.c_str(),S.substr(0,c[0]).c_str()); for(int j=0;j<D-1;j++) fprintf(stderr,"%s|",S.substr(c[2*j+1],c[2*j+2]-c[2*j+1]).c_str()); fprintf(stderr,"%s) tuple(",S.substr(c[2*D-1]).c_str()); for(int j=0;j<D;j++) fprintf(stderr,"%s,",S.substr(c[2*j],c[2*j+1]-c[2*j]).c_str()); fprintf(stderr,")\n");}; fprintf(stderr,"VIOLATION:\n"); pr(it->second.second.first,it->second.second.second); pr(wi,cut);} viol++; } });
  }
  printf("d=%d k=%d words=%zu occurrences=%lld violations=%lld\n",D,K,W.size(),occ,viol);
}
