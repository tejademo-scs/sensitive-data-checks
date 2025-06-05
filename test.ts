import { DOCUMENT } from '@angular/common';
import { Inject, InjectionToken, ModuleWithProviders, NgModule } from '@angular/core';

function clarityScript(projectId: string): string {
  return `(function(c,l,a,r,i,t,y){
    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
  })(window, document, "clarity", "script", "${projectId}");`
}

export const MS_CLARITY_CONFIG_TOKEN = new InjectionToken<MicrosoftClarityConfiguration>('microsoft-clarity.config');

export type MicrosoftClarityConfiguration = Readonly<{
  projectId: string;
}>;

@NgModule()
export class MicrosoftClarityModule {
  constructor(@Inject(DOCUMENT) d: Document, @Inject(MS_CLARITY_CONFIG_TOKEN) { projectId }: MicrosoftClarityConfiguration) {
    const s = d.createElement('script');
    s.type = 'text/javascript';
    s.innerHTML = clarityScript(projectId);
    d.head.appendChild(s);
  }

  static forRoot(config: MicrosoftClarityConfiguration): ModuleWithProviders<MicrosoftClarityModule> {
    return {
      ngModule: MicrosoftClarityModule,
      providers: [{ provide: MS_CLARITY_CONFIG_TOKEN, useValue: config }],
    };
  }
}
