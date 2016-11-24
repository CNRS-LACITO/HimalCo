



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta content="origin-when-cross-origin" name="referrer" />

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-92d354668263723b226099d22b6ff9945593c2bfe41f4403b91481b735f484b0.css" integrity="sha256-ktNUZoJjcjsiYJnSK2/5lFWTwr/kH0QDuRSBtzX0hLA=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-7ec438ba7c15d1510c0d2b3bf1f8c7fcd0f7660c73590fa65e728a279787ca91.css" integrity="sha256-fsQ4unwV0VEMDSs78fjH/ND3ZgxzWQ+mXnKKJ5eHypE=" media="all" rel="stylesheet" />
    
    
    
    

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    
    <title>HimalCo/tex.py at master · CNRS/HimalCo</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://avatars0.githubusercontent.com/u/6152153?v=3&amp;s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="CNRS/HimalCo" name="twitter:title" /><meta content="HimalCo - Himalayan Corpora" name="twitter:description" />
      <meta content="https://avatars0.githubusercontent.com/u/6152153?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="CNRS/HimalCo" property="og:title" /><meta content="https://github.com/CNRS/HimalCo" property="og:url" /><meta content="HimalCo - Himalayan Corpora" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/NjA3MjUyNDoyYWIyYWNhZWMwYWRlODkwMTRlZGQ3MzJiNTBkN2YxZTo4MDU4MDM1ZmRlMjMwYThmNDI3ZDFmYjZkZWI4Yjc3YzNlNWE2MTk4MGFkMDk0ZDUwM2NhMGQ2M2RkYmZlZWEx--b5136e80c62098b7a3267c16b6c4621ad08ba8d1">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">
    <meta name="request-id" content="5CA9F99C:58B4:106E4CD2:58374C36" data-pjax-transient>

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="5CA9F99C:58B4:106E4CD2:58374C36" name="octolytics-dimension-request_id" /><meta content="6072524" name="octolytics-actor-id" /><meta content="alexis-michaud" name="octolytics-actor-login" /><meta content="c6ddb74c0c713acd862c658e03992fcf92cd9954eeed591d9fc4717f9eadf020" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="alexis-michaud">

        <meta name="expected-hostname" content="github.com">
      <meta name="js-proxy-site-detection-payload" content="YzdiZjljYTYzMzIzMDQ5YzgyZjI1YjRhNjE1NDgyNDdlYjM5NjQzZDczNjdiOTlkODg0ZTBlODI1ZDA3N2UyM3x7InJlbW90ZV9hZGRyZXNzIjoiOTIuMTY5LjI0OS4xNTYiLCJyZXF1ZXN0X2lkIjoiNUNBOUY5OUM6NThCNDoxMDZFNENEMjo1ODM3NEMzNiIsInRpbWVzdGFtcCI6MTQ4MDAxOTAwNiwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">


      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta name="html-safe-nonce" content="bc5e7402a6861e67ea6350397e0fb082fa0f39db">
    <meta content="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="bd4e04a76ea53beeba5327650d7c8e7b">
    

      
  <meta name="description" content="HimalCo - Himalayan Corpora">
  <meta name="go-import" content="github.com/CNRS/HimalCo git https://github.com/CNRS/HimalCo.git">

  <meta content="6152153" name="octolytics-dimension-user_id" /><meta content="CNRS" name="octolytics-dimension-user_login" /><meta content="15101737" name="octolytics-dimension-repository_id" /><meta content="CNRS/HimalCo" name="octolytics-dimension-repository_nwo" /><meta content="false" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="15101737" name="octolytics-dimension-repository_network_root_id" /><meta content="CNRS/HimalCo" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/CNRS/HimalCo/commits/master.atom?token=AFyozF3H7WMhZQScHS0mpkFbfl3sM5rzks62Qy0-wA%3D%3D" rel="alternate" title="Recent Commits to HimalCo:master" type="application/atom+xml">


      <link rel="canonical" href="https://github.com/CNRS/HimalCo/blob/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py" data-pjax-transient>
  </head>


  <body class="logged-in  env-production windows vis-private page-blob">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="28" version="1.1" viewBox="0 0 16 16" width="28"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>


        <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/CNRS/HimalCo/search" class="js-site-search-form" data-scoped-search-url="/CNRS/HimalCo/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
    </label>
</form></div>


      <ul class="header-nav float-left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav float-right" id="user-links">
  <li class="header-nav-item">
    
    <a href="/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s js-socket-channel js-notification-indicator" data-channel="tenant:1:notification-changed:6072524" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
        <span class="mail-status unread"></span>
        <svg aria-hidden="true" class="octicon octicon-bell" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <svg aria-hidden="true" class="octicon octicon-plus float-left" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>

  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="CNRS">This organization</span>
  </div>
  <a class="dropdown-item" href="/orgs/CNRS/people#invite-member" data-ga-click="Header, invite someone">
    Invite someone
  </a>
  <a class="dropdown-item" href="/orgs/CNRS/new-team" data-ga-click="Header, create new team">
    New team
  </a>
  <a class="dropdown-item" href="/organizations/CNRS/repositories/new" data-ga-click="Header, create new organization repository, icon:repo">
    New repository
  </a>


  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="CNRS/HimalCo">This repository</span>
  </div>
    <a class="dropdown-item" href="/CNRS/HimalCo/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>
    <a class="dropdown-item" href="/CNRS/HimalCo/settings/collaboration" data-ga-click="Header, create new collaborator">
      New collaborator
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/alexis-michaud"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@alexis-michaud" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/6072524?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">alexis-michaud</strong>
        </div>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/alexis-michaud" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
        <a class="dropdown-item" href="/alexis-michaud?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="i+Hhkqn9JSlOxfIZtbD5BYPg14P658kabfgEGWxxK7ML0kvzAy/LBWCnF8KpuD1rrcz8P2wEz2XrYYilFsUKnQ==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>


      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="RxyBLo0IbyLIwVQFaGL7yxk41OPsflGGDMQGaTrL0BXHLytPJ9qBDuajsd50aj+lNxT/X3qdV/mKXYrVQH/xOw==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="15101737" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/CNRS/HimalCo/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Unwatch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/CNRS/HimalCo/watchers"
            aria-label="6 users are watching this repository">
            6
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/CNRS/HimalCo/unstar" class="starred" data-form-nonce="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="hN75ynmPv/TwQweicT89jbiX2AiwSs+OhCcCIvpYw0QE7VOr011R2N4h4nltN/njlrvztCapyfECvo6egOziag==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar CNRS/HimalCo"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/CNRS/HimalCo/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/CNRS/HimalCo/star" class="unstarred" data-form-nonce="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="BI7sJrCkorJakQLtQTeIMPP9fIxM1ovL9030glsl52uEvUZHGnZMnnTz5zZdP0xe3dFXMNo1jbRx1Hg+IZHGRQ==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star CNRS/HimalCo"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/CNRS/HimalCo/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of CNRS/HimalCo to your account"
              aria-label="Fork your own copy of CNRS/HimalCo to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
            Fork
          </a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header" data-facebox-id="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/CNRS/HimalCo/fork?fragment=1">
              <img alt="Loading" height="64" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" width="64" />
            </include-fragment>
          </div>

    <a href="/CNRS/HimalCo/network" class="social-count"
       aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

    <h1 class="private ">
  <svg aria-hidden="true" class="octicon octicon-lock" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 13H3v-1h1v1zm8-6v7c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h1V4c0-2.2 1.8-4 4-4s4 1.8 4 4v2h1c.55 0 1 .45 1 1zM3.8 6h4.41V4c0-1.22-.98-2.2-2.2-2.2-1.22 0-2.2.98-2.2 2.2v2H3.8zM11 7H2v7h9V7zM4 8H3v1h1V8zm0 2H3v1h1v-1z"/></svg>
  <span class="author" itemprop="author"><a href="/CNRS" class="url fn" rel="author">CNRS</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/CNRS/HimalCo" data-pjax="#js-repo-pjax-container">HimalCo</a></strong>
    <span class="label label-private v-align-middle">Private</span>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/CNRS/HimalCo" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /CNRS/HimalCo" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/CNRS/HimalCo/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /CNRS/HimalCo/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">21</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/CNRS/HimalCo/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /CNRS/HimalCo/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

  <a href="/CNRS/HimalCo/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /CNRS/HimalCo/projects">
    <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
    Projects
    <span class="counter">0</span>
</a>
    <a href="/CNRS/HimalCo/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /CNRS/HimalCo/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a href="/CNRS/HimalCo/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /CNRS/HimalCo/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
    Pulse
</a>
  <a href="/CNRS/HimalCo/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /CNRS/HimalCo/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Graphs
</a>
    <a href="/CNRS/HimalCo/settings" class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations /CNRS/HimalCo/settings">
      <svg aria-hidden="true" class="octicon octicon-gear" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"/></svg>
      Settings
</a>
</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/CNRS/HimalCo/blob/a58bf604a2bae06fac783341c7d29e76c314e27d/dev/lib/pylmflib-1.0/pylmflib/output/tex.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:6ff5bab5028abaa5cc53da101ad2e6d3 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/CNRS/HimalCo/blob/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/CNRS/HimalCo/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" data-form-nonce="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="hefVrD0DYkHFvU2tusKYllUHGk9wM66GOr2FHbcyh4sF1H/Nl9GMbevfqHamylz4eysx8+bQqPm8JAmhzYampQ==" /></div>
          <svg aria-hidden="true" class="octicon octicon-git-branch select-menu-item-icon" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M10 5c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v.3c-.02.52-.23.98-.63 1.38-.4.4-.86.61-1.38.63-.83.02-1.48.16-2 .45V4.72a1.993 1.993 0 0 0-1-3.72C.88 1 0 1.89 0 3a2 2 0 0 0 1 1.72v6.56c-.59.35-1 .99-1 1.72 0 1.11.89 2 2 2 1.11 0 2-.89 2-2 0-.53-.2-1-.53-1.36.09-.06.48-.41.59-.47.25-.11.56-.17.94-.17 1.05-.05 1.95-.45 2.75-1.25S8.95 7.77 9 6.73h-.02C9.59 6.37 10 5.73 10 5zM2 1.8c.66 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2C1.35 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2zm0 12.41c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm6-8c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="dev/lib/pylmflib-1.0/pylmflib/output/tex.py">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/CNRS/HimalCo/tree/khaling_1.0/dev/lib/pylmflib-1.0/pylmflib/output/tex.py"
              data-name="khaling_1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="khaling_1.0">
                khaling_1.0
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="BtnGroup float-right">
    <a href="/CNRS/HimalCo/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/CNRS/HimalCo"><span>HimalCo</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/CNRS/HimalCo/tree/master/dev"><span>dev</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/CNRS/HimalCo/tree/master/dev/lib"><span>lib</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/CNRS/HimalCo/tree/master/dev/lib/pylmflib-1.0"><span>pylmflib-1.0</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/CNRS/HimalCo/tree/master/dev/lib/pylmflib-1.0/pylmflib"><span>pylmflib</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/CNRS/HimalCo/tree/master/dev/lib/pylmflib-1.0/pylmflib/output"><span>output</span></a></span><span class="separator">/</span><strong class="final-path">tex.py</strong>
  </div>
</div>

<include-fragment class="commit-tease" src="/CNRS/HimalCo/contributors/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py">
  <div>
    Fetching contributors&hellip;
  </div>

  <div class="commit-tease-contributors">
    <img alt="" class="loader-loading float-left" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" />
    <span class="loader-error">Cannot retrieve contributors at this time</span>
  </div>
</include-fragment>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/CNRS/HimalCo/raw/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/CNRS/HimalCo/blame/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item">Blame</a>
      <a href="/CNRS/HimalCo/commits/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/CNRS/HimalCo?branch=master&amp;filepath=dev%2Flib%2Fpylmflib-1.0%2Fpylmflib%2Foutput%2Ftex.py"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/CNRS/HimalCo/edit/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py" class="inline-form js-update-url-with-hash" data-form-nonce="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="XS9w9/7KsUnJWRmcIZ9iIzhwhdgBwr91yXuqH+BizcndHNqWVBhfZec7/Ec9l6ZNFlyuZJchuQpP4iajmtbs5w==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Edit this file" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
</form>        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/CNRS/HimalCo/delete/master/dev/lib/pylmflib-1.0/pylmflib/output/tex.py" class="inline-form" data-form-nonce="511a0e0709e3fa6aff30c1a70d54e03af607c5c1" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="/xowcYzBVbbXGL8+tsfvEhb/8lL8F10Bj8eEIShMuvl/KZoQJhO7mvl6WuWqzyt8ONPZ7mr0W34JXgidUvib1w==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      815 lines (771 sloc)
      <span class="file-info-divider"></span>
    41.6 KB
  </div>
</div>

  

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#! /usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @package output</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> config.tex <span class="pl-k">import</span> lmf_to_tex, partOfSpeech_tex</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> config.mdf <span class="pl-k">import</span> mdf_semanticRelation, pd_grammaticalNumber, pd_person, pd_anymacy, pd_clusivity</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> utils.io <span class="pl-k">import</span> open_read, open_write, <span class="pl-c1">EOL</span>, <span class="pl-c1">ENCODING</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> utils.error_handling <span class="pl-k">import</span> OutputError, <span class="pl-c1">Warning</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> common.defs <span class="pl-k">import</span> <span class="pl-c1">VERNACULAR</span>, <span class="pl-c1">ENGLISH</span>, <span class="pl-c1">NATIONAL</span>, <span class="pl-c1">REGIONAL</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># To define languages and fonts</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> config</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">file_read</span>(<span class="pl-smi">filename</span>):</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Read file contents.</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param filename The name of the file with full path containing information to read, for instance the LaTeX header of the document: &#39;user/config/header.tex&#39;.</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A Python string containing read information.</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    contents <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> filename <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">file</span> <span class="pl-k">=</span> open_read(filename)</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">        contents <span class="pl-k">=</span> <span class="pl-v">file</span>.read()</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">file</span>.close()</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> contents</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">insert_references</span>(<span class="pl-smi">lexical_entry</span>):</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Insert references to paradigms.</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The targeted Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing the references in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">    text <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">    part_of_speech <span class="pl-k">=</span> lexical_entry.get_partOfSpeech()</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">    spelling_variant <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(lexical_entry.get_spelling_variants()) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">        spelling_variant <span class="pl-k">=</span> lexical_entry.get_spelling_variants()[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> spelling_variant <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># If current entry is a subentry, then take the spelling variant of the main entry</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">        main_entry <span class="pl-k">=</span> lexical_entry.get_main_entry()</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> main_entry <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(main_entry.get_spelling_variants()) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">                spelling_variant <span class="pl-k">=</span> main_entry.get_spelling_variants()[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> spelling_variant <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> part_of_speech <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>transitive verb<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>hfill<span class="pl-cce">\\</span>break See: <span class="pl-cce">\\</span>ref{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> spelling_variant <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>.vt}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>ref{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> spelling_variant <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>.vt.eng}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> part_of_speech <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>intransitive verb<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>hfill<span class="pl-cce">\\</span>break See: <span class="pl-cce">\\</span>ref{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> spelling_variant <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>.vi}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>ref{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> spelling_variant <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>.vi.eng}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> part_of_speech <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>reflexive verb<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>hfill<span class="pl-cce">\\</span>break See: <span class="pl-cce">\\</span>ref{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> spelling_variant <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>.vr}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>ref{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> spelling_variant <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>.vr.eng}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">tex_write</span>(<span class="pl-smi">object</span>, <span class="pl-smi">filename</span>, <span class="pl-smi">preamble</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">introduction</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">lmf2tex</span><span class="pl-k">=</span>lmf_to_tex, <span class="pl-smi">font</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">items</span><span class="pl-k">=</span><span class="pl-k">lambda</span> <span class="pl-smi">lexical_entry</span>: lexical_entry.get_lexeme(), <span class="pl-smi">sort_order</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">paradigms</span><span class="pl-k">=</span>[], <span class="pl-smi">tables</span><span class="pl-k">=</span>[], <span class="pl-smi">title</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">tex_language</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Write a LaTeX file.</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Note that the lexicon must already be ordered at this point. Here, parameters &#39;items&#39; and &#39;sort_order&#39; are only used to define chapters.</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param object The LMF instance to convert into LaTeX output format.</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param filename The name of the LaTeX file to write with full path, for instance &#39;user/output.tex&#39;.</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param preamble The name of the LaTeX file with full path containing the LaTeX header of the document, for instance &#39;user/config/japhug.tex&#39;. Default value is None.</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param introduction The name of the LaTeX file with full path containing the LaTeX introduction of the document, for instance &#39;user/config/introduction.tex&#39;. Default value is None.</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lmf2tex A function giving the mapping from LMF representation information that must be written to LaTeX commands, in a defined order. Default value is &#39;lmf_to_tex&#39; function defined in &#39;pylmflib/config/tex.py&#39;. Please refer to it as an example.</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param items Lambda function giving the item to sort. Default value is &#39;lambda lexical_entry: lexical_entry.get_lexeme()&#39;, which means that the items to sort are lexemes.</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sort_order Default value is &#39;None&#39;, which means that the LaTeX output is alphabetically ordered.</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param paradigms A Python list of LaTeX filenames with full path containing the paradigms in LaTeX format. Default value is an empty list.</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param tables The name of the LaTeX file with full path containing some notes to add at the end of the LaTeX document, for instance &#39;user/config/conclusion.tex&#39;. Default value is None.</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param title A Python string containing the title of the LaTeX document. Default value is None.</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param tex_language A Python string giving the default language to set in LaTeX.</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> string, os</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Define font</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> font <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">        font <span class="pl-k">=</span> config.xml.font</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    tex_file <span class="pl-k">=</span> open_write(filename)</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Add file header if any</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">    tex_file.write(file_read(preamble))</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Continue the header if needed</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> title <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>title{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> title <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> tex_language <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span>\setdefaultlanguage{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> tex_language <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Insert LaTeX commands to create a document</span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-c1">EOL</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>begin<span class="pl-c1">{document}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>maketitle<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>newpage<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Add introduction if any</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> introduction <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>markboth<span class="pl-c1">{INTRODUCTION}{}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">*</span> <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">    tex_file.write(file_read(introduction))</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Add command for small caps</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-c1">EOL</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>def<span class="pl-cce">\\</span>mytextsc{<span class="pl-cce">\\</span>bgroup<span class="pl-cce">\\</span>obeyspaces<span class="pl-cce">\\</span>mytextscaux}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>def<span class="pl-cce">\\</span>mytextscaux#1{<span class="pl-cce">\\</span>mytextscauxii #1<span class="pl-cce">\\</span>relax<span class="pl-cce">\\</span>relax<span class="pl-cce">\\</span>egroup}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>def<span class="pl-cce">\\</span>mytextscauxii#1{%<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>ifx<span class="pl-cce">\\</span>relax#1<span class="pl-cce">\\</span>else <span class="pl-cce">\\</span>ifcat#1<span class="pl-cce">\\</span>@sptoken<span class="pl-c1">{}</span> <span class="pl-cce">\\</span>expandafter<span class="pl-cce">\\</span>expandafter<span class="pl-cce">\\</span>expandafter<span class="pl-cce">\\</span>mytextscauxii<span class="pl-cce">\\</span>else<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>ifnum`#1=<span class="pl-cce">\\</span>uccode`#1 {<span class="pl-cce">\\</span>normalsize #1}<span class="pl-cce">\\</span>else {<span class="pl-cce">\\</span>footnotesize <span class="pl-cce">\\</span>uppercase{#1}}<span class="pl-cce">\\</span>fi <span class="pl-cce">\\</span>expandafter<span class="pl-cce">\\</span>expandafter<span class="pl-cce">\\</span>expandafter<span class="pl-cce">\\</span>mytextscauxii<span class="pl-cce">\\</span>expandafter<span class="pl-cce">\\</span>fi<span class="pl-cce">\\</span>fi}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">*</span> <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Configure space indent</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>setlength<span class="pl-cce">\\</span>parindent<span class="pl-c1">{0cm}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Insert data path configuration</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Unix-style paths</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    audio_path <span class="pl-k">=</span> config.xml.audio_path</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">    graphic_path <span class="pl-k">=</span> os.path.abspath(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> os.name <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>posix<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Windows-style paths</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">        audio_path <span class="pl-k">=</span> audio_path.replace(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">        graphic_path <span class="pl-k">=</span> graphic_path.replace(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-c1">EOL</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>addmediapath{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> audio_path.rstrip(<span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>addmediapath{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> audio_path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>mp3}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>addmediapath{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> audio_path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>wav}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>graphicspath<span class="pl-c1">{{</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> graphic_path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>/pylmflib/output/img/<span class="pl-c1">}}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">*</span> <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Configure 2 columns</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>newpage<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>begin<span class="pl-c1">{multicols}{2}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">*</span> <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> sort_order <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Lowercase and uppercase letters must have the same rank</span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        sort_order <span class="pl-k">=</span> <span class="pl-c1">dict</span>([(c, <span class="pl-c1">ord</span>(c)) <span class="pl-k">for</span> c <span class="pl-k">in</span> string.lowercase])</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        up <span class="pl-k">=</span> <span class="pl-c1">dict</span>([(c, <span class="pl-c1">ord</span>(c) <span class="pl-k">+</span> <span class="pl-c1">32</span>) <span class="pl-k">for</span> c <span class="pl-k">in</span> string.uppercase])</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        sort_order.update(up)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        sort_order.update({<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>})</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># For each element to write, get the corresponding LMF value</span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">object</span>.<span class="pl-c1">__class__</span>.<span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>LexicalResource<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> lexicon <span class="pl-k">in</span> <span class="pl-c1">object</span>.get_lexicons():</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">            previous_character <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">            current_character <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># Lexicon is already ordered</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> lexical_entry <span class="pl-k">in</span> lexicon.get_lexical_entries():</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># Consider only main entries (subentries and components will be written as parts of the main entry)</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> lexical_entry.find_related_forms(<span class="pl-s"><span class="pl-pds">&quot;</span>main entry<span class="pl-pds">&quot;</span></span>) <span class="pl-k">==</span> [] <span class="pl-k">and</span> lexical_entry.get_independentWord() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"># Check if current element is a lexeme starting with a different character than previous lexeme</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">                        current_character <span class="pl-k">=</span> items(lexical_entry)[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> sort_order[items(lexical_entry)[<span class="pl-c1">0</span>:<span class="pl-c1">1</span>]]:</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">                            current_character <span class="pl-k">=</span> items(lexical_entry)[<span class="pl-c1">0</span>:<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> sort_order[items(lexical_entry)[<span class="pl-c1">0</span>:<span class="pl-c1">2</span>]]:</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                            current_character <span class="pl-k">=</span> items(lexical_entry)[<span class="pl-c1">0</span>:<span class="pl-c1">2</span>]</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span> <span class="pl-c1">IndexError</span>:</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span> <span class="pl-c1">TypeError</span>:</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> ( (<span class="pl-c1">type</span>(sort_order) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">type</span>(<span class="pl-c1">dict</span>())) <span class="pl-k">and</span> ((previous_character <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> (sort_order(current_character) <span class="pl-k">!=</span> sort_order(previous_character))) ) \</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">or</span> ( (<span class="pl-c1">type</span>(sort_order) <span class="pl-k">is</span> <span class="pl-c1">type</span>(<span class="pl-c1">dict</span>())) <span class="pl-k">and</span> (<span class="pl-c1">int</span>(sort_order[current_character]) <span class="pl-k">!=</span> <span class="pl-c1">int</span>(sort_order[previous_character])) ):</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c"># Do not consider special characters</span></td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">                            previous_character <span class="pl-k">=</span> current_character</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">                            tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>newpage<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">                            title <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">if</span> <span class="pl-c1">type</span>(sort_order) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">type</span>(<span class="pl-c1">dict</span>()):</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">                                title <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">NATIONAL</span>](current_character)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">                                <span class="pl-k">for</span> key,value <span class="pl-k">in</span> <span class="pl-c1">sorted</span>(sort_order.items(), <span class="pl-v">key</span><span class="pl-k">=</span><span class="pl-k">lambda</span> <span class="pl-smi">x</span>: x[<span class="pl-c1">1</span>]):</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-k">if</span> <span class="pl-c1">int</span>(value) <span class="pl-k">==</span> <span class="pl-c1">int</span>(sort_order[current_character]):</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">                                        title <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](key)</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">                            tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>section*{<span class="pl-cce">\\</span>centering-<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> handle_reserved(title) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> -}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                            <span class="pl-c">#tex_file.write(&quot;\\pdfbookmark[1]{&quot; + title + &quot; }{&quot; + title + &quot; }&quot; + EOL)</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">                        tex_file.write(lmf2tex(lexical_entry, font))</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> <span class="pl-c1">len</span>(paradigms) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">                            tex_file.write(insert_references(lexical_entry))</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">                         <span class="pl-c"># tex_file.write(&quot;\\lhead{\\firstmark}&quot; + EOL)</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">                         <span class="pl-c"># tex_file.write(&quot;\\rhead{\\botmark}&quot; + EOL)</span></td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">						 <span class="pl-c"># On sépare les entrées lexicales par des lignes vides</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c"># Separate lexical entries from each others with a blank line</span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">                        tex_file.write(<span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c"># Handle subentries</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">for</span> related_form <span class="pl-k">in</span> lexical_entry.get_related_forms(<span class="pl-s"><span class="pl-pds">&quot;</span>subentry<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">if</span> related_form.get_lexical_entry() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">                                tex_file.write(lmf2tex(related_form.get_lexical_entry(), font))</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">                                <span class="pl-k">if</span> <span class="pl-c1">len</span>(paradigms) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">                                    tex_file.write(insert_references(related_form.get_lexical_entry()))</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">                                <span class="pl-c"># Separate sub-entries from each others with a blank line</span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">                                tex_file.write(<span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> <span class="pl-c1">Warning</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Cannot sort item <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> items(lexical_entry).encode(<span class="pl-c1">ENCODING</span>))</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span> <span class="pl-c1">IndexError</span>:</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c"># Item is an empty string</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> OutputError(<span class="pl-c1">object</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Object to write must be a Lexical Resource.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Insert LaTeX commands to finish the document properly</span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span>\end<span class="pl-c1">{multicols}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Insert paradigms if any</span></td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> filename <span class="pl-k">in</span> paradigms:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>newpage<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span>\markboth<span class="pl-c1">{paradigms}{}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">        tex_file.write(file_read(filename))</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Insert other tables if any</span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> filename <span class="pl-k">in</span> tables:</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>newpage<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">        tex_file.write(file_read(filename))</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">        tex_file.write(<span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">    tex_file.write(<span class="pl-s"><span class="pl-pds">&quot;</span>\end<span class="pl-c1">{document}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span>)</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">    tex_file.close()</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line"><span class="pl-c">## Functions to process LaTeX layout</span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_font</span>(<span class="pl-smi">text</span>):</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Replace &#39;{xxx}&#39; by &#39;\ipa{xxx}&#39; in &#39;un&#39;, &#39;xn&#39;, &#39;gn&#39;, &#39;dn&#39;, &#39;en&#39;.</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">    pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-cce">\\\|</span><span class="pl-c1">]</span><span class="pl-k">*</span>){(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">}</span><span class="pl-c1">]</span><span class="pl-k">*</span>)}(<span class="pl-c1">.</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">while</span> re.match(pattern, text):</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(pattern, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>ipa{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_reserved</span>(<span class="pl-smi">text</span>):</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span> Handle reserved characters $ &amp; % # _ ^ except \ { }.</span></td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>$<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>$<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>\$<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># In some LaTeX commands, &#39;$&#39; must not be replaced by &#39;\$&#39; =&gt; marked as &#39;\\dollar&#39; in this case</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>dollar<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>dollar<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>$<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>&amp; <span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>&amp; <span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>\&amp; <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>%<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>%<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>\%<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>#<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>#<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>\#<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>\string_<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>^<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>^<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>U+005E<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_fi</span>(<span class="pl-smi">text</span>):</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Replace &#39;fi:xxx&#39; and &#39;|fi{xxx}&#39; by <span class="pl-cce">\\</span>textit{xxx}.</span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>fi:<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">        pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)fi:(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">\s</span><span class="pl-cce">\.</span><span class="pl-c1">,)</span><span class="pl-c1">]</span><span class="pl-k">*</span>)(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(pattern, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>|fi{<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">        pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-cce">\|</span>fi{(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">}</span><span class="pl-c1">]</span><span class="pl-k">*</span>)}(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(pattern, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_fv</span>(<span class="pl-smi">text</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Replace &#39;fv:xxx&#39; and &#39;|fv{xxx}&#39; by font[VERNACULAR](xxx).</span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>fv:<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#pattern = r&quot;(.*[ }])?fv:([^\s\.,)]*)(.*)&quot;</span></td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">        pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)fv:(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">\s</span><span class="pl-cce">\.</span><span class="pl-c1">,)</span><span class="pl-c1">]</span><span class="pl-k">*</span>)(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(pattern, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>%s<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> font[<span class="pl-c1">VERNACULAR</span>](<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>).replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>).replace(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span>2<span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>|fv{<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">        pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-cce">\|</span>fv{(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">}</span><span class="pl-c1">]</span><span class="pl-k">*</span>)}(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(pattern, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>%s<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> font[<span class="pl-c1">VERNACULAR</span>](<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>).replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>).replace(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span>2<span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_fn</span>(<span class="pl-smi">text</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Replace &#39;fn:xxx&#39; and &#39;|fn{xxx}&#39; by font[NATIONAL](xxx).</span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>fn:<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">        pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)fn:(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">\s</span><span class="pl-cce">\.</span><span class="pl-c1">,)</span><span class="pl-c1">]</span><span class="pl-k">*</span>)(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(pattern, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>%s<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> font[<span class="pl-c1">NATIONAL</span>](<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>).replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>).replace(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span>2<span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>|fn{<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">        pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-cce">\|</span>fn{(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">}</span><span class="pl-c1">]</span><span class="pl-k">*</span>)}(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(pattern, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>%s<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> font[<span class="pl-c1">NATIONAL</span>](<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>).replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>).replace(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span>2<span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_pinyin</span>(<span class="pl-smi">text</span>):</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Replace &#39;@xxx&#39; by &#39;<span class="pl-cce">\\</span>textcolor{gray}{xxx}&#39; in &#39;lx&#39;, &#39;dv&#39;, &#39;xv&#39; fields (already in API).</span></td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>@<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)@(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textcolor{gray}{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span>, text)</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_caps</span>(<span class="pl-smi">text</span>):</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Handle small caps.</span></td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Replace &#39;°xxx&#39; by &#39;<span class="pl-cce">\t</span>extsc{xxx}&#39; in translated examples.</span></td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.encode(<span class="pl-s"><span class="pl-pds">&quot;</span>utf8<span class="pl-pds">&quot;</span></span>).find(<span class="pl-s"><span class="pl-pds">&quot;</span>°<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># LaTeX does not support &#39;#&#39; nor &#39;_&#39; characters inside &#39;\mytextsc&#39; command</span></td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> re.sub(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>(<span class="pl-c1">\w</span><span class="pl-k">*</span>)°(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-c1">\s</span><span class="pl-cce">\.</span><span class="pl-c1">,)+/:</span><span class="pl-cce">\#\_</span><span class="pl-c1">]</span><span class="pl-k">*</span>)(<span class="pl-c1">\w</span><span class="pl-k">*</span>)<span class="pl-pds">&quot;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\1</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textsc{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\2</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-ent">\3</span><span class="pl-pds">&quot;</span></span>, text.encode(<span class="pl-s"><span class="pl-pds">&quot;</span>utf8<span class="pl-pds">&quot;</span></span>)).decode(<span class="pl-s"><span class="pl-pds">&quot;</span>utf8<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">handle_quotes</span>(<span class="pl-smi">text</span>):</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Hanlde quotation marks.</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Replace each &quot;xxx&quot; by ``xxx&quot;.</span></td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">    pattern <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-c1">^</span>(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-cce">\&quot;</span><span class="pl-c1">]</span><span class="pl-k">*</span>)<span class="pl-cce">\&quot;</span>(<span class="pl-c1">[</span><span class="pl-k">^</span><span class="pl-cce">\&quot;</span><span class="pl-c1">]</span><span class="pl-k">*</span>)<span class="pl-cce">\&quot;</span><span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> re.match(pattern, text)</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">    end <span class="pl-k">=</span> text</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">    text <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">while</span> result:</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">+=</span> result.group(<span class="pl-c1">1</span>) <span class="pl-k">+</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>``<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> result.group(<span class="pl-c1">2</span>) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">        end <span class="pl-k">=</span> end.replace(result.group(<span class="pl-c1">1</span>) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> result.group(<span class="pl-c1">2</span>) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">=</span> re.match(pattern, end)</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">    text <span class="pl-k">+=</span> end</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line"><span class="pl-c">## Functions to process LaTeX fields (output)</span></td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_uid</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Transform unique identifier of a lexical entry in ASCII format.</span></td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The targeted Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing the unique identifier in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># LaTeX does not handle &#39;\&#39; (backslash), &#39;{&#39; (left brace) and &#39;{&#39; (right brace) characters in links</span></td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">    text <span class="pl-k">=</span> lexical_entry.get_id()</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&quot;</span>£<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>{<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>{<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>\{<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> text.find(<span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span>) <span class="pl-k">!=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> text.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>}<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>\}<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_link</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display hyperlink to a lexical entry in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The targeted Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing the hyperlink in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>hyperlink{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> format_uid(lexical_entry, font) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](lexical_entry.get_lexeme())</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_homonymNumber() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-cce">\\</span>textsubscript{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(lexical_entry.get_homonymNumber()) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_lexeme</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief &#39;lx&#39;, &#39;hm&#39; and &#39;lc&#39; fields are flipped if &#39;lc&#39; field has data.</span></td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing lexeme in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">    lexeme <span class="pl-k">=</span> font[<span class="pl-c1">VERNACULAR</span>](lexical_entry.get_lexeme())</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.is_subentry():</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>subparagraph{<span class="pl-cce">\\</span>dollar<span class="pl-cce">\\</span>blacksquare<span class="pl-cce">\\</span>dollar <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>paragraph{<span class="pl-cce">\\</span>hspace{-0.5cm} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_homonymNumber() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Add homonym number to lexeme</span></td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">        lexeme <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-cce">\\</span>textsubscript{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(lexical_entry.get_homonymNumber()) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_contextual_variations() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(lexical_entry.get_contextual_variations()) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Format contextual variations</span></td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> var <span class="pl-k">in</span> lexical_entry.get_contextual_variations():</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](var)</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> (from: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexeme <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>).<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Format lexeme</span></td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> lexeme</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-cce">\\</span>hypertarget{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> format_uid(lexical_entry, font) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-c1">{}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> lexical_entry.is_subentry():</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>\markboth{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexeme <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-c1">{}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_audio</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Embed sound file into PDF.</span></td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string embedding sound in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">from</span> os.path <span class="pl-k">import</span> basename, isfile</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># To access options</span></td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">from</span> pylmflib <span class="pl-k">import</span> options</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> options</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> options.audio:</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> form_representation <span class="pl-k">in</span> lexical_entry.get_form_representations():</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> form_representation.get_audio() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># Embed local sound file</span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># \includemedia[&lt;options&gt;]{&lt;poster text&gt;}{&lt;main Flash (SWF) file or URL  |  3D (PRC, U3D) file&gt;}</span></td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># To include audio file in PDF, replace WAV extension by MP3 extension and search in audio, MP3 and WAV folders</span></td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">            file_name <span class="pl-k">=</span> form_representation.get_audio().get_fileName().replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.wav<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>.mp3<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">            file_path <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> os.name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>posix<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># Unix-style paths</span></td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">                file_path.append(config.xml.audio_path <span class="pl-k">+</span> file_name)</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">                file_path.append(config.xml.audio_path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>mp3/<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> file_name)</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">                file_path.append(config.xml.audio_path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>wav/<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> file_name)</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># Windows-style paths</span></td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">                audio_path <span class="pl-k">=</span> config.xml.audio_path.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">                file_path.append(audio_path <span class="pl-k">+</span> file_name)</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">                file_path.append(audio_path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>mp3<span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> file_name)</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">                file_path.append(audio_path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>wav<span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> file_name)</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">            exist <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> audio_file <span class="pl-k">in</span> file_path:</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> isfile(audio_file):</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">                    exist <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> exist:</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> <span class="pl-c1">Warning</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Sound file &#39;<span class="pl-c1">%s</span>&#39; encountered for lexeme &#39;<span class="pl-c1">%s</span>&#39; does not exist<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (file_name.encode(<span class="pl-c1">ENCODING</span>), lexical_entry.get_lexeme().encode(<span class="pl-c1">ENCODING</span>)))</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">            file_name <span class="pl-k">=</span> file_name.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>\string-<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>\includemedia[<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span>addresource=<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> file_name <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>,<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span>flashvars={<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t\t</span>source=<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> file_name <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t\t</span>&amp;autoPlay=true<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t\t</span>&amp;autoRewind=true<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t\t</span>&amp;loop=false<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t\t</span>&amp;hideBar=true<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t\t</span>&amp;volume=1.0<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t\t</span>&amp;balance=0.0<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span>\</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>}]{\includegraphics[scale=0.5]{sound.jpg}}{APlayer.swf}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># \mediabutton[&lt;options&gt;]{&lt;normal button text or graphic&gt;}</span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-cce">\\</span>hspace{0.1cm}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_part_of_speech</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>, <span class="pl-smi">mapping</span><span class="pl-k">=</span>partOfSpeech_tex, <span class="pl-smi">language</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display part of speech in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param mapping A Python dictionary giving the mapping between LMF part of speech LexicalEntry attribute value and LaTeX layout.</span></td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param language Language to consider to display part of speech.</span></td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing part of speech in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_partOfSpeech() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> language <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">                result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> mapping[lexical_entry.get_partOfSpeech()] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">                result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> mapping[(language, lexical_entry.get_partOfSpeech())] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> <span class="pl-c1">Warning</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Part of speech value &#39;<span class="pl-c1">%s</span>&#39; encountered for lexeme &#39;<span class="pl-c1">%s</span>&#39; is not defined in configuration<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (lexical_entry.get_partOfSpeech().encode(<span class="pl-c1">ENCODING</span>), lexical_entry.get_lexeme().encode(<span class="pl-c1">ENCODING</span>)))</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_definitions</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>, <span class="pl-smi">languages</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Glosses are supplanted by definitions.</span></td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sense The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param languages A list of languages to consider for definitions and glosses (all by default).</span></td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing glosses and definitions in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> languages <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">        languages <span class="pl-k">=</span> [config.xml.vernacular, config.xml.English, config.xml.national, config.xml.regional]</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> language <span class="pl-k">in</span> languages:</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(sense.find_definitions(language)) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> definition <span class="pl-k">in</span> sense.find_definitions(language):</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> language <span class="pl-k">==</span> config.xml.vernacular:</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> font[<span class="pl-c1">VERNACULAR</span>](definition) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> language <span class="pl-k">==</span> config.xml.national:</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> font[<span class="pl-c1">NATIONAL</span>](handle_font(definition)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> language <span class="pl-k">==</span> config.xml.regional:</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Regnl: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">REGIONAL</span>](definition) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]}. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> definition <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-c1">len</span>(sense.find_glosses(language)) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> gloss <span class="pl-k">in</span> sense.find_glosses(language):</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> language <span class="pl-k">==</span> config.xml.vernacular:</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> font[<span class="pl-c1">VERNACULAR</span>](gloss) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> language <span class="pl-k">==</span> config.xml.national:</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> font[<span class="pl-c1">NATIONAL</span>](handle_font(gloss)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> language <span class="pl-k">==</span> config.xml.regional:</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Regnl: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">REGIONAL</span>](gloss) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]}. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> gloss <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(sense.get_translations(language)) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> translation <span class="pl-k">in</span> sense.get_translations(language):</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> language <span class="pl-k">==</span> config.xml.national:</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> font[<span class="pl-c1">NATIONAL</span>](translation) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> language <span class="pl-k">==</span> config.xml.regional:</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textbf<span class="pl-c1">{rr<span class="pl-c1">:</span>}</span><span class="pl-cce">\\</span>textit{[Regnl: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> translation <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]}. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">                    result <span class="pl-k">+=</span> translation <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_lt</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display &#39;lt&#39; in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sense The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing &#39;lt&#39; in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># return &quot;\\textit{Lit:} &quot; + u&quot;\u2018&quot; + sense.get_lt() + u&quot;\u2019&quot; + &quot;. &quot;</span></td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_sc</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display &#39;sc&#39; in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sense The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing &#39;sc&#39; in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># return &quot;\\textit{\uline{&quot; + sense.get_sc() + &quot;}}. &quot;</span></td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_rf</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display &#39;rf&#39; in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing &#39;rf&#39; in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># return &quot;\\textit{Ref:} &quot; + sense.get_rf() + &quot; &quot;</span></td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_examples</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>, <span class="pl-smi">languages</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display examples in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sense The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param languages A list of languages to consider for examples (all by default).</span></td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing examples in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> languages <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">        languages <span class="pl-k">=</span> [config.xml.vernacular, config.xml.English, config.xml.national, config.xml.regional]</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> context <span class="pl-k">in</span> sense.get_contexts():</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">        tmp <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> language <span class="pl-k">in</span> languages:</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> example <span class="pl-k">in</span> context.find_written_forms(language):</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> language <span class="pl-k">==</span> config.xml.vernacular:</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">                    tmp <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>sn <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](example) <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> language <span class="pl-k">==</span> config.xml.national:</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">                    tmp <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>trans <span class="pl-cce">\\</span>textit{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">NATIONAL</span>](handle_font(example)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> language <span class="pl-k">==</span> config.xml.regional:</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">                    tmp <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>trans <span class="pl-cce">\\</span>textit{[<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">REGIONAL</span>](example) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]}<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>: <span class="pl-c"># language == config.xml.English</span></td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">                    tmp <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>trans <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> example <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># LaTeX does not support empty examples</span></td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(tmp) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>begin<span class="pl-c1">{exe}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span> <span class="pl-k">+</span> tmp <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>end<span class="pl-c1">{exe}</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">EOL</span></td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_usage_notes</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display usage notes in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sense The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing usage notes in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> usage <span class="pl-k">in</span> sense.find_usage_notes(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.vernacular):</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{VerUsage<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](usage) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> usage <span class="pl-k">in</span> sense.find_usage_notes(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.English):</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Usage<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> usage <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> usage <span class="pl-k">in</span> sense.find_usage_notes(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.national):</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">NATIONAL</span>](handle_font(usage)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> usage <span class="pl-k">in</span> sense.find_usage_notes(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.regional):</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">REGIONAL</span>](usage) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_encyclopedic_informations</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display encyclopedic informations in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sense The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing encyclopedic informations in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> information <span class="pl-k">in</span> sense.find_encyclopedic_informations(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.vernacular):</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> font[<span class="pl-c1">VERNACULAR</span>](information) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> information <span class="pl-k">in</span> sense.find_encyclopedic_informations(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.English):</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> information <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> information <span class="pl-k">in</span> sense.find_encyclopedic_informations(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.national):</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> font[<span class="pl-c1">NATIONAL</span>](handle_font(information)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> information <span class="pl-k">in</span> sense.find_encyclopedic_informations(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.regional):</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">REGIONAL</span>](information) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_restrictions</span>(<span class="pl-smi">sense</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display restrictions in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param sense The current Sense LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing restrictions in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> restriction <span class="pl-k">in</span> sense.find_restrictions(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.vernacular):</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{VerRestrict<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](restriction) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> restriction <span class="pl-k">in</span> sense.find_restrictions(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.English):</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Restrict<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> restriction <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> restriction <span class="pl-k">in</span> sense.find_restrictions(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.national):</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">NATIONAL</span>](restriction) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> restriction <span class="pl-k">in</span> sense.find_restrictions(<span class="pl-v">language</span><span class="pl-k">=</span>config.xml.regional):</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">REGIONAL</span>](restriction) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_lexical_functions</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display lexical functions in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing lexical functions in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += &quot;\\textit{&quot; + lexical_entry.get_lf() + &quot;: }&quot;</span></td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += lexical_entry.get_le() + &quot; &quot;</span></td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += lexical_entry.get_ln() + &quot; &quot;</span></td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += lexical_entry.get_lr() + &quot; &quot;</span></td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_related_forms</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>, <span class="pl-smi">language</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display related forms in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param language Language to consider to display related forms.</span></td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing related forms in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> related_form <span class="pl-k">in</span> lexical_entry.get_related_forms(mdf_semanticRelation[<span class="pl-s"><span class="pl-pds">&quot;</span>sy<span class="pl-pds">&quot;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Syn<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> related_form.get_lexical_entry() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> format_link(related_form.get_lexical_entry(), font)</td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> font[<span class="pl-c1">VERNACULAR</span>](related_form.get_lexeme())</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> related_form <span class="pl-k">in</span> lexical_entry.get_related_forms(mdf_semanticRelation[<span class="pl-s"><span class="pl-pds">&quot;</span>an<span class="pl-pds">&quot;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Ant<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> related_form.get_lexical_entry() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> format_link(related_form.get_lexical_entry(), font)</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> font[<span class="pl-c1">VERNACULAR</span>](related_form.get_lexeme())</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> morphology <span class="pl-k">in</span> lexical_entry.get_morphologies():</td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Morph<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](morphology) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> related_form <span class="pl-k">in</span> lexical_entry.get_related_forms(mdf_semanticRelation[<span class="pl-s"><span class="pl-pds">&quot;</span>cf<span class="pl-pds">&quot;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> language <span class="pl-k">==</span> config.xml.English:</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{See<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{Voir :} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> related_form.get_lexical_entry() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> format_link(related_form.get_lexical_entry(), font)</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> font[<span class="pl-c1">VERNACULAR</span>](related_form.get_lexeme())</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># ce</span></td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># cn</span></td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># cr</span></td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += &quot;\\textit{See main entry:} &quot; + font[VERNACULAR](lexical_entry.get_mn()) + &quot;. &quot;</span></td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_variant_forms</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display variant forms in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing variant forms in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> form_representation <span class="pl-k">in</span> lexical_entry.get_form_representations():</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> form_representation.get_variantForm() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Variant<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">VERNACULAR</span>](form_representation.get_variantForm()) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> form_representation.get_comment(config.xml.English) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span>  <span class="pl-s"><span class="pl-pds">&quot;</span>(<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> form_representation.get_comment(config.xml.English) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>) <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> form_representation.get_comment(config.xml.national) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span>  <span class="pl-s"><span class="pl-pds">&quot;</span>(<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">NATIONAL</span>](form_representation.get_comment(config.xml.national)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>) <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> form_representation.get_comment(config.xml.regional) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span>  <span class="pl-s"><span class="pl-pds">&quot;</span>(<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> font[<span class="pl-c1">REGIONAL</span>](form_representation.get_comment(config.xml.regional)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>) <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_borrowed_word</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display borrowed word in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing borrowed word in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_borrowed_word() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{From<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexical_entry.get_borrowed_word()</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> lexical_entry.get_written_form() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">            result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexical_entry.get_written_form()</td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_etymology</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display etymology in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing etymology in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_etymology() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Etym<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexical_entry.get_etymology() <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_etymology_gloss() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&quot;</span><span class="pl-cce">\u2018</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexical_entry.get_etymology_gloss() <span class="pl-k">+</span> <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&quot;</span><span class="pl-cce">\u2019</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_paradigms</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display all paradigms in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing all paradigms in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms():</td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Prdm<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>}. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&quot;</span>sg<span class="pl-pds">&quot;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Sg<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&quot;</span>pl<span class="pl-pds">&quot;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Pl<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += &quot;\\textit{Redup:} \\textbf{&quot; + lexical_entry.get_rd() + &quot;} &quot;</span></td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">1</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>s<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{1s<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">2</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>s<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{2s<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">3</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>s<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{3s<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">anymacy</span><span class="pl-k">=</span>pd_anymacy[<span class="pl-c1">4</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>s<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{3sn<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">1</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>d<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{1d<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">2</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>d<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{2d<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">3</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>d<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{3d<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">anymacy</span><span class="pl-k">=</span>pd_anymacy[<span class="pl-c1">4</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>d<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{3dn<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">1</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>p<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{1p<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">1</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>p<span class="pl-pds">&#39;</span></span>], <span class="pl-v">clusivity</span><span class="pl-k">=</span>pd_clusivity[<span class="pl-s"><span class="pl-pds">&#39;</span>e<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{1px<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">1</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>p<span class="pl-pds">&#39;</span></span>], <span class="pl-v">clusivity</span><span class="pl-k">=</span>pd_clusivity[<span class="pl-s"><span class="pl-pds">&#39;</span>i<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{1pi<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">2</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>p<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{2p<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">person</span><span class="pl-k">=</span>pd_person[<span class="pl-c1">3</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>p<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{3p<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> paradigm <span class="pl-k">in</span> lexical_entry.find_paradigms(<span class="pl-v">anymacy</span><span class="pl-k">=</span>pd_anymacy[<span class="pl-c1">4</span>], <span class="pl-v">grammatical_number</span><span class="pl-k">=</span>pd_grammaticalNumber[<span class="pl-s"><span class="pl-pds">&#39;</span>p<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{3pn<span class="pl-c1">:</span>}</span> <span class="pl-cce">\\</span>textbf{<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> paradigm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_table</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display a table in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing a table in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_semantic_domains</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display semantic domains in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing semantic domains in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> semantic_domain <span class="pl-k">in</span> lexical_entry.get_semantic_domains():</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{SD<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> semantic_domain <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># is</span></td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += &quot;\\textit{Semantics:} &quot; + lexical_entry.get_is() + &quot;. &quot;</span></td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># th</span></td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># result += &quot;\\textit{Thes:} &quot; + lexical_entry.get_th() + &quot;. &quot;</span></td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_bibliography</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display bibliography in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing bibliography in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_bibliography() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Read<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexical_entry.get_bibliography() <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_picture</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display a picture in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing a picture in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># return &quot;(&quot; + lexical_entry.get_pc() + &quot;) &quot;</span></td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_notes</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display all notes in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing all notes in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> note <span class="pl-k">in</span> lexical_entry.find_notes(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>general<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Note: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> note <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> note <span class="pl-k">in</span> lexical_entry.find_notes(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>phonology<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Phon: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> note <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> note <span class="pl-k">in</span> lexical_entry.find_notes(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>grammar<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Gram: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> note <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> note <span class="pl-k">in</span> lexical_entry.find_notes(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>discourse<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Disc: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> note <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> note <span class="pl-k">in</span> lexical_entry.find_notes(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>anthropology<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Ant: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> note <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> note <span class="pl-k">in</span> lexical_entry.find_notes(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>sociolinguistics<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Socio: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> note <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> note <span class="pl-k">in</span> lexical_entry.find_notes(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>question<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit{[Ques: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> note <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>]} <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_source</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display source in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing source in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># return &quot;\\textit{Source:} &quot; + lexical_entry.get_so() + &quot;. &quot;</span></td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_status</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Display status in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return A string representing status in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> lexical_entry.get_status() <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>textit<span class="pl-c1">{Status<span class="pl-c1">:</span>}</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> lexical_entry.get_status()</td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_date</span>(<span class="pl-smi">lexical_entry</span>, <span class="pl-smi">font</span>):</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>! @brief Do not display date in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param lexical_entry The current Lexical Entry LMF instance.</span></td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.</span></td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    @return An empty string.</span></td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
</table>

  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.15539s from github-fe153-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
      </button>
      You can't perform that action at this time.
    </div>


      
      <script crossorigin="anonymous" integrity="sha256-q1D7/rLAuHSPor/tXQvMz8BrgKvykFhqfRxvI5AvXfM=" src="https://assets-cdn.github.com/assets/frameworks-ab50fbfeb2c0b8748fa2bfed5d0bcccfc06b80abf290586a7d1c6f23902f5df3.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-7ueovoPeAq1yt0hl7zaTSNcsvvC2zgdnMRyn0fqv1Ao=" src="https://assets-cdn.github.com/assets/github-eee7a8be83de02ad72b74865ef369348d72cbef0b6ce0767311ca7d1faafd40a.js"></script>
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>

  </body>
</html>

