# wabde-widgets

This is a collection of widgets intended for use
with a [Docker project](https://github.com/Wildsong/docker-wabde)
that helps you to put together and maintain
a development environment for the
"Esri Web AppBuilder, Developer Edition" aka "WABDE".

Each standard Esri widget that comes packaged with WABDE
is licensed under Apache 2.0.

I have put each widget into a github project and include it here as a submodule.

So far they are all identical to the widgets from WABDE.

I will be adding more widgets from other sources tomorrow.

Brian Wilson <brian@wildsong.biz>

## Widget sources

All the Esri sourced submodules have the name Wildsong/wabde-widget-*

"PublicNotification" is from Esri but not included in WABDE.

There are some third party widgets, including
* PopupPanel
* SaveSession
* Table (which I am writing now and does currently nothing useful yet except test the build process!)

There are lists of some widget names in
scripts/esri-wabde-list (complete list from version 2.19)
and scripts/third-party-list (some are already included as submodules, working on the others)

## Other Esri files in this repo

There were some little files in clients/stemapp/widgets and I have not
figured out another way to get them into the right place yet, so I
stuck them in this repo.Putting them here means you just do a clone
into widgets and everything is good to go; all submodules (widgets) and these files.

They are all covered under Apache 2.0 and copyright ESRI.

```
main.js
package.js
package.json
widgets.d.ts
```

BTW I have not figured out what they do yet either. I assume that the WABDe uses them
when building applications over in server/apps to include the widgets?? Whatever. For now
I just assume they have to be here. Maybe they do nothing at all. ;-)

## References

[Esri Developer site](https://developer.esri.com)

