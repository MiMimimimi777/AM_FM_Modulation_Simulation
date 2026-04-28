#include "bits/stdc++.h"
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	
	int n;cin>>n;
	vector<pair<int,int>> v;
	vector<int> t;
	for(int i=1;i<=n;++i)
	{
		int x;cin>>x;
		t.push_back(x);
		v.push_back({x,i});
	}
	sort(v.begin(),v.end());
	sort(t.begin(),t.end());
	
	int mx=v[n-1].first;
	bool first=true;
	for(auto i:v)
	{
		if(mx==i.first)
		{
			if(!first)cout<<' ';
			cout<<i.second;
			first=false;
		}
	}
	cout<<'\n';
	int m;cin>>m;
	while(m--)
	{
		int x;cin>>x;
		auto it=upper_bound(t.begin(),t.end(),x);
		int idx=it-t.begin();
		if(it!=t.end())cout<<v[idx].second<<'\n';
		else cout<<0<<'\n';
	}
	
	return 0;
}