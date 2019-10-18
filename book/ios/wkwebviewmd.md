p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 15.0px Menlo; color: \#6c7986; background-color: \#1f1f24}  
p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 15.0px Menlo; color: \#ffffff; background-color: \#1f1f24; min-height: 18.0px}

// \[self.webView setOpaque:NO\];

// self.webView.scrollView.backgroundColor = \[UIColor colorGrayBG\];

//  改变网页内容背景颜色

// \[self.webView evaluateJavaScript:@"document.getElementsByTagName\('body'\)\[0\].style.background='\#000000'"completionHandler:nil\];

// \[self.webView evaluateJavaScript:@"document.body.style.backgroundColor=\"\#1E1E1E\"" completionHandler:nil\];

// //OC调用JS changeColor\(\)是JS方法名，completionHandler是异步回调block

// NSString \*jsString = \[NSString stringWithFormat:@"changeColor\('%@'\)", @"document.getElementsByTagName\('body'\)\[0\].style.background='\#333333'"\];

// \[\_webView evaluateJavaScript:jsString completionHandler:^\(id \_Nullable data, NSError \* \_Nullable error\) {

// NSLog\(@"改变HTML的背景色"\);

// }\];

// // 改变网页内容文字颜色

// \[self.webView evaluateJavaScript:@"document.getElementsByTagName\('body'\)\[0\].style.webkitTextFillColor= '\#8F999999'"completionHandler:nil\];

// for \(UIView \*subView in \[webView subviews\]\) {

//

// if \(\[subView isKindOfClass:\[UIScrollView class\]\]\) {

//

// for \(UIView \*shadowView in \[subView subviews\]\) {

//

// if \(\[shadowView isKindOfClass:\[UIImageView class\]\]\) {

//

// shadowView.hidden = YES;

//

// }

//

// }

//

// }

//

// }

// dispatch\_after\(dispatch\_time\(DISPATCH\_TIME\_NOW, \(int64\_t\)\(0.1 \* NSEC\_PER\_SEC\)\), dispatch\_get\_main\_queue\(\), ^{

// CGRect frame = self.webView.frame;

// frame.size.width = SCREEN\_WIDTH;

// frame.size.height = 1;

// // webView.scrollView.scrollEnabled = NO;

// self.webView.frame = frame;

// frame.size.height = self.webView.scrollView.contentSize.height;

// NSLog\(@"frame = %@", \[NSValue valueWithCGRect:frame\]\);

// self.webView.frame = frame;

// }\);









  
p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 15.0px Menlo; color: \#fd8f3f; background-color: \#1f1f24}  
p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 15.0px Menlo; color: \#ffffff; background-color: \#1f1f24; min-height: 18.0px}  
p.p3 {margin: 0.0px 0.0px 0.0px 0.0px; font: 15.0px Menlo; color: \#ffffff; background-color: \#1f1f24}  
p.p4 {margin: 0.0px 0.0px 0.0px 0.0px; font: 15.0px Menlo; color: \#fc6a5d; background-color: \#1f1f24}  
p.p5 {margin: 0.0px 0.0px 0.0px 0.0px; font: 15.0px Menlo; color: \#6c7986; background-color: \#1f1f24}  
span.s1 {color: \#fc5fa3}  
span.s2 {color: \#7ac8b6}  
span.s3 {color: \#fd8f3f}  
span.s4 {color: \#fc6a5d}  
span.s5 {color: \#ffffff}  
span.s6 {color: \#99e8d5}  
span.s7 {color: \#aef37d}  
span.s8 {color: \#91d462}  


\#pragma mark - WKScriptMessageHandler

  


- \(**void**\)userContentController:\(WKUserContentController \*\)userContentController didReceiveScriptMessage:\(WKScriptMessage \*\)message {



NSLog\(@"body:%@", message.body\);



**if**\(\[message.nameisEqualToString:@"ShowMessageFromWKWebView"\]\) {

 \[**self**showMessageWithParams:message.body\];

 }

}

\#pragma mark

\#pragma mark - Show Message

  


- \(**void**\)showMessageWithParams:\(NSDictionary \*\)dict {



**if** \(!\[dict isKindOfClass:\[NSDictionaryclass\]\]\) {

**return**;

 }



NSString \*messageStr = \[dict objectForKey:@"message"\];

NSString \*titleStr = \[dict objectForKey:@"title"\];

NSLog\(@"title:%@", titleStr\);

NSLog\(@"messageStr:%@", messageStr\);



// do it



// 将结果返回给js

NSString\*returnJSStr = \[NSStringstringWithFormat:@"showMessageFromWKWebViewResult\('%@'\)", @"message传到OC成功"\];

 \[**self**.webViewevaluateJavaScript:returnJSStr completionHandler:^\(**id\_Nullable** result, NSError \* **\_Nullable** error\) {



NSLog\(@"%@,%@", result, error\);

 }\];

}

