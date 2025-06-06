using Eventuous.GooglePubSub.Subscriptions;
using Eventuous.Subscriptions.Filters;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;

namespace IntegrationsHub.V2.Infrastructure.PubSub.DomainEvents;

public sealed class LegacyIntegrationEventsPubSubSubscription : IntegrationDomainEventsBasePubSubSubscription
{
    public LegacyIntegrationEventsPubSubSubscription(
        IOptions<IntegrationDomainEventsPubSubSettings> settings,
        PubSubSubscriptionOptions subscriptionOptions,
        ConsumePipe consumePipe,
        ILoggerFactory loggerFactory)
        : base(settings, ConfigureSubscriptionId(subscriptionOptions, settings.Value.LegacyEventsSubscriptionId), consumePipe, loggerFactory) { }
    
    static PubSubSubscriptionOptions ConfigureSubscriptionId(
        PubSubSubscriptionOptions options,
        string subscriptionId
    )
    {
        options.SubscriptionId = subscriptionId;

        return options;
    }
}
